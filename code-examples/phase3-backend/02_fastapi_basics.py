"""
FASTAPI REST API - COMPLETE EXAMPLE
Learn backend development with Python and FastAPI

Topics covered:
- FastAPI setup
- Path operations (routes)
- Request/Response models (Pydantic)
- Path parameters and query parameters
- Authentication with JWT
- CRUD operations
- Data validation
- Error handling
- API documentation (automatic!)
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime, timedelta
import jwt
from passlib.context import CryptContext

# ============================================
# APP SETUP
# ============================================

app = FastAPI(
    title="Todo API",
    description="A complete REST API example with FastAPI",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
SECRET_KEY = "your-secret-key-change-in-production"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()

# In-memory data store (use database in production)
users_db = []
todos_db = []
next_user_id = 1
next_todo_id = 1

# ============================================
# PYDANTIC MODELS (Data Validation)
# ============================================

class UserRegister(BaseModel):
    """Model for user registration"""
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)

class UserLogin(BaseModel):
    """Model for user login"""
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    """Model for user response (without password)"""
    id: int
    username: str
    email: str
    created_at: datetime

class TodoCreate(BaseModel):
    """Model for creating a todo"""
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None

class TodoUpdate(BaseModel):
    """Model for updating a todo"""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    completed: Optional[bool] = None

class TodoResponse(BaseModel):
    """Model for todo response"""
    id: int
    user_id: int
    title: str
    description: str
    completed: bool
    created_at: datetime
    updated_at: datetime

class Token(BaseModel):
    """Model for authentication token"""
    access_token: str
    token_type: str

# ============================================
# HELPER FUNCTIONS
# ============================================

def hash_password(password: str) -> str:
    """Hash a password"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against hash"""
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(user_id: int) -> str:
    """Create JWT access token"""
    expire = datetime.utcnow() + timedelta(days=7)
    to_encode = {"user_id": user_id, "exp": expire}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> int:
    """
    Dependency to get current authenticated user
    This runs before protected route handlers
    """
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials"
            )
        
        # Check if user exists
        user = next((u for u in users_db if u["id"] == user_id), None)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found"
            )
        
        return user_id
        
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired"
        )
    except jwt.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

# ============================================
# AUTHENTICATION ROUTES
# ============================================

@app.post("/api/auth/register", response_model=dict, status_code=status.HTTP_201_CREATED)
async def register(user_data: UserRegister):
    """
    Register a new user
    
    - **username**: User's username (3-50 characters)
    - **email**: Valid email address
    - **password**: Password (minimum 6 characters)
    """
    global next_user_id
    
    # Check if user exists
    if any(u["email"] == user_data.email for u in users_db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )
    
    # Create user
    user = {
        "id": next_user_id,
        "username": user_data.username,
        "email": user_data.email,
        "password": hash_password(user_data.password),
        "created_at": datetime.utcnow()
    }
    next_user_id += 1
    users_db.append(user)
    
    # Generate token
    token = create_access_token(user["id"])
    
    return {
        "user": UserResponse(**{k: v for k, v in user.items() if k != "password"}),
        "access_token": token,
        "token_type": "bearer"
    }

@app.post("/api/auth/login", response_model=dict)
async def login(credentials: UserLogin):
    """
    Login with email and password
    
    Returns access token for authentication
    """
    # Find user
    user = next((u for u in users_db if u["email"] == credentials.email), None)
    
    if not user or not verify_password(credentials.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    # Generate token
    token = create_access_token(user["id"])
    
    return {
        "user": UserResponse(**{k: v for k, v in user.items() if k != "password"}),
        "access_token": token,
        "token_type": "bearer"
    }

@app.get("/api/auth/me", response_model=UserResponse)
async def get_me(user_id: int = Depends(get_current_user)):
    """Get current authenticated user"""
    user = next((u for u in users_db if u["id"] == user_id), None)
    return UserResponse(**{k: v for k, v in user.items() if k != "password"})

# ============================================
# TODO CRUD ROUTES
# ============================================

@app.get("/api/todos", response_model=List[TodoResponse])
async def get_todos(
    user_id: int = Depends(get_current_user),
    completed: Optional[bool] = None,
    skip: int = 0,
    limit: int = 100
):
    """
    Get all todos for current user
    
    - **completed**: Filter by completion status (optional)
    - **skip**: Number of items to skip (pagination)
    - **limit**: Maximum number of items to return
    """
    user_todos = [t for t in todos_db if t["user_id"] == user_id]
    
    # Filter by completion status
    if completed is not None:
        user_todos = [t for t in user_todos if t["completed"] == completed]
    
    # Pagination
    return user_todos[skip:skip + limit]

@app.get("/api/todos/{todo_id}", response_model=TodoResponse)
async def get_todo(todo_id: int, user_id: int = Depends(get_current_user)):
    """Get a specific todo by ID"""
    todo = next((t for t in todos_db if t["id"] == todo_id and t["user_id"] == user_id), None)
    
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )
    
    return todo

@app.post("/api/todos", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
async def create_todo(todo_data: TodoCreate, user_id: int = Depends(get_current_user)):
    """
    Create a new todo
    
    - **title**: Todo title (required, 1-200 characters)
    - **description**: Todo description (optional)
    """
    global next_todo_id
    
    todo = {
        "id": next_todo_id,
        "user_id": user_id,
        "title": todo_data.title,
        "description": todo_data.description or "",
        "completed": False,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    next_todo_id += 1
    todos_db.append(todo)
    
    return todo

@app.put("/api/todos/{todo_id}", response_model=TodoResponse)
async def update_todo(
    todo_id: int,
    todo_data: TodoUpdate,
    user_id: int = Depends(get_current_user)
):
    """Update a todo"""
    todo = next((t for t in todos_db if t["id"] == todo_id and t["user_id"] == user_id), None)
    
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )
    
    # Update fields
    if todo_data.title is not None:
        todo["title"] = todo_data.title
    if todo_data.description is not None:
        todo["description"] = todo_data.description
    if todo_data.completed is not None:
        todo["completed"] = todo_data.completed
    
    todo["updated_at"] = datetime.utcnow()
    
    return todo

@app.delete("/api/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int, user_id: int = Depends(get_current_user)):
    """Delete a todo"""
    global todos_db
    
    todo_index = next((i for i, t in enumerate(todos_db) 
                      if t["id"] == todo_id and t["user_id"] == user_id), None)
    
    if todo_index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )
    
    todos_db.pop(todo_index)
    return

@app.patch("/api/todos/{todo_id}/toggle", response_model=TodoResponse)
async def toggle_todo(todo_id: int, user_id: int = Depends(get_current_user)):
    """Toggle todo completion status"""
    todo = next((t for t in todos_db if t["id"] == todo_id and t["user_id"] == user_id), None)
    
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )
    
    todo["completed"] = not todo["completed"]
    todo["updated_at"] = datetime.utcnow()
    
    return todo

# ============================================
# PUBLIC ROUTES
# ============================================

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Todo API with FastAPI",
        "version": "1.0.0",
        "documentation": "/docs",
        "endpoints": {
            "auth": {
                "register": "POST /api/auth/register",
                "login": "POST /api/auth/login",
                "me": "GET /api/auth/me"
            },
            "todos": {
                "list": "GET /api/todos",
                "get": "GET /api/todos/{id}",
                "create": "POST /api/todos",
                "update": "PUT /api/todos/{id}",
                "delete": "DELETE /api/todos/{id}",
                "toggle": "PATCH /api/todos/{id}/toggle"
            }
        }
    }

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "OK",
        "timestamp": datetime.utcnow().isoformat(),
        "users": len(users_db),
        "todos": len(todos_db)
    }

"""
============================================
TO RUN THIS SERVER:
============================================

1. Install dependencies:
   pip install fastapi uvicorn python-jose[cryptography] passlib[bcrypt] python-multipart

2. Run server:
   uvicorn 02_fastapi_basics:app --reload

3. Access interactive API documentation:
   http://localhost:8000/docs  (Swagger UI)
   http://localhost:8000/redoc (ReDoc)

4. Test with curl or use /docs interactive interface:

   # Register
   curl -X POST http://localhost:8000/api/auth/register \
     -H "Content-Type: application/json" \
     -d '{"username":"john","email":"john@example.com","password":"password123"}'

   # Login
   curl -X POST http://localhost:8000/api/auth/login \
     -H "Content-Type: application/json" \
     -d '{"email":"john@example.com","password":"password123"}'

   # Create todo (replace YOUR_TOKEN)
   curl -X POST http://localhost:8000/api/todos \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_TOKEN" \
     -d '{"title":"Learn FastAPI","description":"Build REST API"}'

============================================
LEARNING NOTES:
============================================

1. FASTAPI ADVANTAGES:
   - Automatic API documentation (Swagger/ReDoc)
   - Data validation with Pydantic
   - Type hints for better IDE support
   - High performance (async/await)
   - Easy to learn and use

2. PYDANTIC MODELS:
   - Automatic data validation
   - Type conversion
   - JSON serialization
   - Documentation generation

3. DEPENDENCY INJECTION:
   - Depends() for reusable dependencies
   - Authentication middleware
   - Database connections
   - Configuration

4. ASYNC/AWAIT:
   - async def for async operations
   - await for async calls
   - Better performance for I/O operations

5. AUTOMATIC DOCUMENTATION:
   - Visit /docs for interactive API docs
   - Try endpoints directly from browser
   - See all models and schemas

============================================
NEXT STEPS:
============================================

1. Connect to database (SQLAlchemy + PostgreSQL)
2. Add proper database models
3. Add file upload endpoints
4. Add WebSocket support
5. Add background tasks (Celery)
6. Add caching (Redis)
7. Add tests (pytest)
8. Deploy to cloud (Docker + AWS/Heroku)
"""

