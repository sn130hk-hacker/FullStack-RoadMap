"""
ML WEB INTEGRATION - COMPLETE EXAMPLE
Integrate Machine Learning with FastAPI web application

This example shows:
- Loading pre-trained ML models
- Creating ML-powered API endpoints
- Data validation with Pydantic
- Prediction serving
- Model versioning
- Error handling
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from typing import List, Dict, Optional
import numpy as np
import pandas as pd
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import logging
from datetime import datetime

# ============================================
# SETUP & MODEL TRAINING
# ============================================

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Train and save a model (in production, load pre-trained model)
def train_and_save_model():
    """Train a simple model for demonstration"""
    logger.info("Training model...")
    
    # Load data
    iris = load_iris()
    X, y = iris.data, iris.target
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Train scaler
    scaler = StandardScaler()
    scaler.fit(X_train)
    
    # Save models
    joblib.dump(model, 'iris_model.pkl')
    joblib.dump(scaler, 'iris_scaler.pkl')
    
    # Save metadata
    metadata = {
        'model_type': 'RandomForestClassifier',
        'features': list(iris.feature_names),
        'classes': list(iris.target_names),
        'accuracy': float(model.score(X_test, y_test)),
        'trained_at': datetime.now().isoformat(),
        'version': '1.0.0'
    }
    joblib.dump(metadata, 'model_metadata.pkl')
    
    logger.info(f"Model trained with accuracy: {metadata['accuracy']:.4f}")
    return model, scaler, metadata

# Initialize model on startup
try:
    model = joblib.load('iris_model.pkl')
    scaler = joblib.load('iris_scaler.pkl')
    metadata = joblib.load('model_metadata.pkl')
    logger.info("Loaded existing model")
except FileNotFoundError:
    model, scaler, metadata = train_and_save_model()

# ============================================
# FASTAPI APP SETUP
# ============================================

app = FastAPI(
    title="ML Prediction API",
    description="Machine Learning model serving with FastAPI",
    version="1.0.0"
)

# ============================================
# PYDANTIC MODELS (DATA VALIDATION)
# ============================================

class IrisFeatures(BaseModel):
    """Input features for Iris prediction"""
    sepal_length: float = Field(..., ge=0, le=10, description="Sepal length in cm")
    sepal_width: float = Field(..., ge=0, le=10, description="Sepal width in cm")
    petal_length: float = Field(..., ge=0, le=10, description="Petal length in cm")
    petal_width: float = Field(..., ge=0, le=10, description="Petal width in cm")
    
    @validator('*')
    def check_positive(cls, v):
        if v < 0:
            raise ValueError('Value must be positive')
        return v
    
    class Config:
        schema_extra = {
            "example": {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
                "petal_width": 0.2
            }
        }

class BatchPredictionRequest(BaseModel):
    """Batch prediction request"""
    samples: List[IrisFeatures] = Field(..., min_items=1, max_items=100)

class PredictionResponse(BaseModel):
    """Prediction response"""
    prediction: str
    confidence: float
    probabilities: Dict[str, float]
    model_version: str

class BatchPredictionResponse(BaseModel):
    """Batch prediction response"""
    predictions: List[PredictionResponse]
    total_samples: int

class ModelInfo(BaseModel):
    """Model information"""
    model_type: str
    features: List[str]
    classes: List[str]
    accuracy: float
    trained_at: str
    version: str

# ============================================
# HELPER FUNCTIONS
# ============================================

def prepare_features(features: IrisFeatures) -> np.ndarray:
    """Convert Pydantic model to numpy array"""
    return np.array([[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]])

def make_prediction(features: np.ndarray) -> Dict:
    """Make prediction with model"""
    try:
        # Scale features
        features_scaled = scaler.transform(features)
        
        # Get prediction and probabilities
        prediction = model.predict(features_scaled)[0]
        probabilities = model.predict_proba(features_scaled)[0]
        
        # Get class name
        class_name = metadata['classes'][prediction]
        
        # Get confidence (probability of predicted class)
        confidence = float(probabilities[prediction])
        
        # Create probability dictionary
        prob_dict = {
            class_name: float(prob) 
            for class_name, prob in zip(metadata['classes'], probabilities)
        }
        
        return {
            'prediction': class_name,
            'confidence': confidence,
            'probabilities': prob_dict,
            'model_version': metadata['version']
        }
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

# ============================================
# API ENDPOINTS
# ============================================

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "ML Prediction API",
        "version": "1.0.0",
        "model": metadata['model_type'],
        "endpoints": {
            "predict": "POST /predict",
            "predict_batch": "POST /predict/batch",
            "model_info": "GET /model/info",
            "health": "GET /health"
        }
    }

@app.post("/predict", response_model=PredictionResponse)
async def predict(features: IrisFeatures):
    """
    Make a single prediction
    
    Predicts Iris flower species based on measurements
    """
    logger.info(f"Received prediction request: {features.dict()}")
    
    # Prepare features
    feature_array = prepare_features(features)
    
    # Make prediction
    result = make_prediction(feature_array)
    
    logger.info(f"Prediction: {result['prediction']} (confidence: {result['confidence']:.2f})")
    
    return result

@app.post("/predict/batch", response_model=BatchPredictionResponse)
async def predict_batch(request: BatchPredictionRequest):
    """
    Make batch predictions
    
    Predicts multiple samples at once (max 100)
    """
    logger.info(f"Received batch prediction request: {len(request.samples)} samples")
    
    predictions = []
    
    for sample in request.samples:
        feature_array = prepare_features(sample)
        result = make_prediction(feature_array)
        predictions.append(result)
    
    return {
        "predictions": predictions,
        "total_samples": len(predictions)
    }

@app.get("/model/info", response_model=ModelInfo)
async def get_model_info():
    """
    Get model information
    
    Returns metadata about the current model
    """
    return metadata

@app.get("/health")
async def health_check():
    """
    Health check endpoint
    
    Verifies that model is loaded and ready
    """
    try:
        # Test prediction to ensure model works
        test_features = np.array([[5.1, 3.5, 1.4, 0.2]])
        test_pred = model.predict(scaler.transform(test_features))
        
        return {
            "status": "healthy",
            "model_loaded": True,
            "model_version": metadata['version'],
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        raise HTTPException(status_code=503, detail="Service unhealthy")

@app.post("/model/reload")
async def reload_model():
    """
    Reload model from disk
    
    Useful for updating to new model version without restarting server
    """
    global model, scaler, metadata
    
    try:
        model = joblib.load('iris_model.pkl')
        scaler = joblib.load('iris_scaler.pkl')
        metadata = joblib.load('model_metadata.pkl')
        
        logger.info(f"Model reloaded successfully. Version: {metadata['version']}")
        
        return {
            "message": "Model reloaded successfully",
            "version": metadata['version'],
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Model reload failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Model reload failed: {str(e)}")

# ============================================
# STARTUP AND SHUTDOWN EVENTS
# ============================================

@app.on_event("startup")
async def startup_event():
    """Run on application startup"""
    logger.info("=" * 60)
    logger.info("ML Prediction API Starting...")
    logger.info(f"Model: {metadata['model_type']}")
    logger.info(f"Version: {metadata['version']}")
    logger.info(f"Accuracy: {metadata['accuracy']:.4f}")
    logger.info("=" * 60)

@app.on_event("shutdown")
async def shutdown_event():
    """Run on application shutdown"""
    logger.info("ML Prediction API Shutting down...")

"""
============================================
TO RUN THIS SERVER:
============================================

1. Install dependencies:
   pip install fastapi uvicorn scikit-learn joblib numpy pandas

2. Run server:
   uvicorn 02_ml_web_integration:app --reload

3. Access interactive docs:
   http://localhost:8000/docs

4. Test with curl:

   # Single prediction
   curl -X POST http://localhost:8000/predict \
     -H "Content-Type: application/json" \
     -d '{
       "sepal_length": 5.1,
       "sepal_width": 3.5,
       "petal_length": 1.4,
       "petal_width": 0.2
     }'

   # Batch prediction
   curl -X POST http://localhost:8000/predict/batch \
     -H "Content-Type: application/json" \
     -d '{
       "samples": [
         {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2},
         {"sepal_length": 6.7, "sepal_width": 3.1, "petal_length": 4.7, "petal_width": 1.5}
       ]
     }'

   # Model info
   curl http://localhost:8000/model/info

============================================
INTEGRATION WITH FRONTEND:
============================================

// JavaScript example
async function predictFlower(features) {
    const response = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(features)
    });
    
    const result = await response.json();
    console.log('Prediction:', result.prediction);
    console.log('Confidence:', result.confidence);
    return result;
}

// Usage
const features = {
    sepal_length: 5.1,
    sepal_width: 3.5,
    petal_length: 1.4,
    petal_width: 0.2
};

predictFlower(features).then(result => {
    console.log(result);
});

============================================
PRODUCTION CONSIDERATIONS:
============================================

1. ✅ Authentication:
   - Add API keys or JWT authentication
   - Rate limiting per user

2. ✅ Monitoring:
   - Log all predictions
   - Track model performance
   - Set up alerts for errors

3. ✅ Caching:
   - Cache predictions for identical inputs
   - Use Redis for distributed caching

4. ✅ Model Versioning:
   - Store multiple model versions
   - A/B test different models
   - Gradual rollout

5. ✅ Scalability:
   - Use async processing for batch predictions
   - Deploy with Docker + Kubernetes
   - Load balancing

6. ✅ Error Handling:
   - Graceful degradation
   - Fallback models
   - Proper error messages

============================================
NEXT STEPS:
============================================

1. Deploy to cloud (AWS, GCP, Azure)
2. Add more ML models (NLP, Computer Vision)
3. Implement model retraining pipeline
4. Add monitoring dashboard
5. Integrate with frontend application
6. Add batch processing with Celery
7. Implement feature store
8. Add model explainability (SHAP, LIME)
"""

