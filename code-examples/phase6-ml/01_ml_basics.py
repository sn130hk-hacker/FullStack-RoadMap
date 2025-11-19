"""
MACHINE LEARNING BASICS - COMPLETE EXAMPLE
Learn ML fundamentals with practical examples

Topics covered:
- Data preprocessing
- Train/test split
- Classification (Logistic Regression, Random Forest)
- Regression (Linear Regression)
- Model evaluation
- Feature engineering
- Model persistence (save/load)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report,
    mean_squared_error, r2_score
)
import joblib
import warnings
warnings.filterwarnings('ignore')

print("=" * 60)
print("MACHINE LEARNING BASICS - LEARNING GUIDE")
print("=" * 60)

# ============================================
# 1. DATA LOADING AND EXPLORATION
# ============================================

print("\n" + "=" * 60)
print("1. DATA LOADING AND EXPLORATION")
print("=" * 60)

# Create sample dataset (Iris-like data for classification)
from sklearn.datasets import load_iris, load_boston

# Load Iris dataset (classification)
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target
iris_df['species'] = iris_df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

print("\n📊 Iris Dataset (Classification)")
print(f"Shape: {iris_df.shape}")
print(f"\nFirst few rows:")
print(iris_df.head())
print(f"\nDataset info:")
print(iris_df.info())
print(f"\nStatistical summary:")
print(iris_df.describe())
print(f"\nClass distribution:")
print(iris_df['species'].value_counts())

# ============================================
# 2. DATA PREPROCESSING
# ============================================

print("\n" + "=" * 60)
print("2. DATA PREPROCESSING")
print("=" * 60)

# Separate features and target
X = iris_df.drop(['target', 'species'], axis=1)
y = iris_df['target']

print(f"\nFeatures shape: {X.shape}")
print(f"Target shape: {y.shape}")

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\nTraining set size: {len(X_train)}")
print(f"Testing set size: {len(X_test)}")

# Feature scaling (important for many ML algorithms)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"\nBefore scaling - mean: {X_train.mean().mean():.2f}, std: {X_train.std().mean():.2f}")
print(f"After scaling - mean: {X_train_scaled.mean():.2f}, std: {X_train_scaled.std():.2f}")

# ============================================
# 3. CLASSIFICATION - LOGISTIC REGRESSION
# ============================================

print("\n" + "=" * 60)
print("3. CLASSIFICATION - LOGISTIC REGRESSION")
print("=" * 60)

# Train logistic regression model
lr_model = LogisticRegression(random_state=42, max_iter=200)
lr_model.fit(X_train_scaled, y_train)

# Make predictions
y_pred_lr = lr_model.predict(X_test_scaled)

# Evaluate model
accuracy_lr = accuracy_score(y_test, y_pred_lr)
print(f"\n✅ Accuracy: {accuracy_lr:.4f} ({accuracy_lr*100:.2f}%)")

print(f"\n📊 Classification Report:")
print(classification_report(y_test, y_pred_lr, target_names=iris.target_names))

print(f"\n🎯 Confusion Matrix:")
cm_lr = confusion_matrix(y_test, y_pred_lr)
print(cm_lr)

# Cross-validation score
cv_scores_lr = cross_val_score(lr_model, X_train_scaled, y_train, cv=5)
print(f"\n🔄 Cross-validation scores: {cv_scores_lr}")
print(f"   Average CV score: {cv_scores_lr.mean():.4f} (+/- {cv_scores_lr.std() * 2:.4f})")

# ============================================
# 4. CLASSIFICATION - RANDOM FOREST
# ============================================

print("\n" + "=" * 60)
print("4. CLASSIFICATION - RANDOM FOREST")
print("=" * 60)

# Train random forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)  # Random Forest doesn't require scaling

# Make predictions
y_pred_rf = rf_model.predict(X_test)

# Evaluate model
accuracy_rf = accuracy_score(y_test, y_pred_rf)
print(f"\n✅ Accuracy: {accuracy_rf:.4f} ({accuracy_rf*100:.2f}%)")

print(f"\n📊 Classification Report:")
print(classification_report(y_test, y_pred_rf, target_names=iris.target_names))

# Feature importance
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=False)

print(f"\n🎯 Feature Importance:")
print(feature_importance)

# ============================================
# 5. REGRESSION EXAMPLE
# ============================================

print("\n" + "=" * 60)
print("5. REGRESSION EXAMPLE")
print("=" * 60)

# Create sample regression data
np.random.seed(42)
X_reg = np.random.rand(100, 1) * 10
y_reg = 2.5 * X_reg + 1.5 + np.random.randn(100, 1) * 2

# Split data
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)

# Train linear regression model
reg_model = LinearRegression()
reg_model.fit(X_train_reg, y_train_reg)

# Make predictions
y_pred_reg = reg_model.predict(X_test_reg)

# Evaluate model
mse = mean_squared_error(y_test_reg, y_pred_reg)
rmse = np.sqrt(mse)
r2 = r2_score(y_test_reg, y_pred_reg)

print(f"\n📈 Model coefficients:")
print(f"   Slope: {reg_model.coef_[0][0]:.4f}")
print(f"   Intercept: {reg_model.intercept_[0]:.4f}")

print(f"\n✅ Evaluation Metrics:")
print(f"   Mean Squared Error (MSE): {mse:.4f}")
print(f"   Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"   R² Score: {r2:.4f}")

# ============================================
# 6. MAKING PREDICTIONS
# ============================================

print("\n" + "=" * 60)
print("6. MAKING PREDICTIONS")
print("=" * 60)

# Make predictions on new data
new_sample = [[5.1, 3.5, 1.4, 0.2]]  # Iris sample
new_sample_scaled = scaler.transform(new_sample)

# Predict with both models
pred_lr = lr_model.predict(new_sample_scaled)[0]
pred_rf = rf_model.predict(new_sample)[0]

# Get prediction probabilities
prob_lr = lr_model.predict_proba(new_sample_scaled)[0]
prob_rf = rf_model.predict_proba(new_sample)[0]

print(f"\n🔮 Predictions for new sample: {new_sample[0]}")
print(f"\nLogistic Regression:")
print(f"   Predicted class: {iris.target_names[pred_lr]}")
print(f"   Probabilities: {dict(zip(iris.target_names, prob_lr.round(3)))}")

print(f"\nRandom Forest:")
print(f"   Predicted class: {iris.target_names[pred_rf]}")
print(f"   Probabilities: {dict(zip(iris.target_names, prob_rf.round(3)))}")

# ============================================
# 7. MODEL PERSISTENCE (SAVE/LOAD)
# ============================================

print("\n" + "=" * 60)
print("7. MODEL PERSISTENCE (SAVE/LOAD)")
print("=" * 60)

# Save models
joblib.dump(lr_model, 'logistic_regression_model.pkl')
joblib.dump(rf_model, 'random_forest_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("\n✅ Models saved:")
print("   - logistic_regression_model.pkl")
print("   - random_forest_model.pkl")
print("   - scaler.pkl")

# Load models (demonstration)
loaded_lr_model = joblib.load('logistic_regression_model.pkl')
loaded_scaler = joblib.load('scaler.pkl')

# Test loaded model
test_pred = loaded_lr_model.predict(loaded_scaler.transform(new_sample))
print(f"\n🔄 Loaded model prediction: {iris.target_names[test_pred[0]]}")

# ============================================
# 8. PRACTICAL ML TIPS
# ============================================

print("\n" + "=" * 60)
print("8. PRACTICAL ML TIPS")
print("=" * 60)

tips = """
✅ DATA PREPARATION:
   • Always explore your data first
   • Handle missing values
   • Scale features for distance-based algorithms
   • Split data before any preprocessing (avoid data leakage)

✅ MODEL SELECTION:
   • Start simple (Logistic Regression, Linear Regression)
   • Try ensemble methods (Random Forest, Gradient Boosting)
   • Use cross-validation for robust evaluation
   • Compare multiple models

✅ EVALUATION:
   • Use appropriate metrics (accuracy, F1, RMSE, etc.)
   • Check confusion matrix for classification
   • Plot learning curves
   • Validate on unseen data

✅ IMPROVEMENT:
   • Feature engineering (create new features)
   • Hyperparameter tuning (GridSearchCV, RandomizedSearchCV)
   • Try different algorithms
   • Collect more data if possible

✅ PRODUCTION:
   • Save models with joblib or pickle
   • Version your models
   • Monitor model performance
   • Retrain periodically
"""

print(tips)

# ============================================
# 9. EXAMPLE USE CASES
# ============================================

print("\n" + "=" * 60)
print("9. COMMON ML USE CASES")
print("=" * 60)

use_cases = """
📊 CLASSIFICATION:
   • Email spam detection
   • Image classification
   • Sentiment analysis
   • Disease diagnosis
   • Customer churn prediction

📈 REGRESSION:
   • House price prediction
   • Stock price forecasting
   • Sales forecasting
   • Temperature prediction
   • Demand forecasting

🎯 CLUSTERING:
   • Customer segmentation
   • Image compression
   • Anomaly detection
   • Document grouping

💡 RECOMMENDATION:
   • Product recommendations (e-commerce)
   • Content recommendations (Netflix, YouTube)
   • Friend suggestions (social media)
"""

print(use_cases)

# ============================================
# 10. NEXT STEPS
# ============================================

print("\n" + "=" * 60)
print("10. NEXT STEPS FOR LEARNING")
print("=" * 60)

next_steps = """
1️⃣  Deep Learning:
   • Neural Networks with TensorFlow/PyTorch
   • Convolutional Neural Networks (CNN) for images
   • Recurrent Neural Networks (RNN) for sequences

2️⃣  Advanced Topics:
   • Natural Language Processing (NLP)
   • Computer Vision
   • Time Series Analysis
   • Reinforcement Learning

3️⃣  MLOps:
   • Model deployment (Flask, FastAPI)
   • Model monitoring
   • A/B testing
   • CI/CD for ML

4️⃣  Practice Projects:
   • Kaggle competitions
   • Build end-to-end ML applications
   • Deploy models to production
   • Contribute to open-source ML projects
"""

print(next_steps)

print("\n" + "=" * 60)
print("🎉 You've learned ML basics! Keep practicing!")
print("=" * 60)

"""
============================================
TO RUN THIS SCRIPT:
============================================

1. Install dependencies:
   pip install numpy pandas matplotlib seaborn scikit-learn joblib

2. Run script:
   python 01_ml_basics.py

3. Output files created:
   - logistic_regression_model.pkl
   - random_forest_model.pkl
   - scaler.pkl

============================================
PRACTICE EXERCISES:
============================================

1. Load a different dataset from sklearn.datasets
2. Try different classification algorithms (SVM, KNN)
3. Implement hyperparameter tuning with GridSearchCV
4. Create visualizations for model results
5. Build a complete ML pipeline with sklearn.pipeline
6. Handle imbalanced datasets
7. Implement custom feature engineering

============================================
RECOMMENDED DATASETS FOR PRACTICE:
============================================

• sklearn.datasets.load_wine() - Wine classification
• sklearn.datasets.load_breast_cancer() - Cancer detection
• sklearn.datasets.load_diabetes() - Diabetes regression
• sklearn.datasets.fetch_california_housing() - Housing prices
• Kaggle datasets - Real-world data
"""

