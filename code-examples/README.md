# Code Examples & Learning Resources

This directory contains **hands-on code examples** with detailed explanations to help you learn full-stack development with ML.

---

## 📁 Directory Structure

```
code-examples/
├── phase1-foundations/          # Programming basics
├── phase2-frontend/             # HTML, CSS, React examples
├── phase3-backend/              # Node.js, Python backend examples
├── phase4-database/             # Database examples (coming soon)
├── phase5-devops/               # Docker, deployment examples (coming soon)
├── phase6-ml/                   # Machine Learning examples
└── exercises/                   # Practice exercises with solutions
```

---

## 🎯 How to Use These Resources

### 1. **Read the Code**
- Each file has extensive comments explaining every concept
- Code is organized in sections for easy learning
- Real-world examples you can run and modify

### 2. **Run the Examples**
- Follow the instructions at the top of each file
- Install required dependencies
- Run and see the output
- Experiment by changing code

### 3. **Practice Exercises**
- Complete exercises to reinforce learning
- Solutions are included for reference
- Try solving before looking at solutions

### 4. **Build Projects**
- Use these examples as templates
- Combine concepts to build real projects
- Modify and extend the examples

---

## 📚 Phase 1: Foundations

### Python Basics (`phase1-foundations/01_python_basics.py`)
**What you'll learn:**
- Variables and data types
- Control structures (if/else, loops)
- Functions
- Lists and dictionaries
- Classes and OOP
- File operations
- Error handling

**Run it:**
```bash
python code-examples/phase1-foundations/01_python_basics.py
```

### JavaScript Basics (`phase1-foundations/02_javascript_basics.js`)
**What you'll learn:**
- Variables (let, const)
- Data types and operators
- Functions and arrow functions
- Arrays and array methods
- Objects and classes
- Async/await
- Modern ES6+ features

**Run it:**
```bash
node code-examples/phase1-foundations/02_javascript_basics.js
```

---

## 🎨 Phase 2: Frontend Development

### HTML & CSS Basics (`phase2-frontend/01_html_css_basics.html`)
**What you'll learn:**
- Semantic HTML5
- CSS Flexbox and Grid
- Responsive design
- CSS animations and transitions
- Modern CSS techniques
- Form styling
- Card components

**Run it:**
```bash
# Open in browser
open code-examples/phase2-frontend/01_html_css_basics.html
# or
google-chrome code-examples/phase2-frontend/01_html_css_basics.html
```

### React Todo App (`phase2-frontend/02_react_todo_app.jsx`)
**What you'll learn:**
- React components
- useState and useEffect hooks
- Props and event handling
- Conditional rendering
- List rendering with keys
- Local storage integration
- Component composition

**Setup:**
```bash
# Create React app
npx create-react-app my-todo-app
cd my-todo-app

# Copy the component file
# Replace src/App.js with the code from 02_react_todo_app.jsx

# Run
npm start
```

---

## 🔧 Phase 3: Backend Development

### Express.js API (`phase3-backend/01_express_api_basics.js`)
**What you'll learn:**
- Express.js setup
- RESTful API design
- Middleware
- Authentication with JWT
- CRUD operations
- Error handling
- Input validation

**Setup & Run:**
```bash
# Install dependencies
npm init -y
npm install express cors jsonwebtoken bcrypt

# Run server
node code-examples/phase3-backend/01_express_api_basics.js

# Server runs on http://localhost:3000
```

**Test it:**
```bash
# Register user
curl -X POST http://localhost:3000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username":"john","email":"john@example.com","password":"password123"}'

# Create todo (use token from register response)
curl -X POST http://localhost:3000/api/todos \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"title":"Learn Express","description":"Build REST API"}'
```

### FastAPI Backend (`phase3-backend/02_fastapi_basics.py`)
**What you'll learn:**
- FastAPI setup
- Pydantic models for validation
- Path and query parameters
- JWT authentication
- Automatic API documentation
- Async/await in Python
- Error handling

**Setup & Run:**
```bash
# Install dependencies
pip install fastapi uvicorn python-jose[cryptography] passlib[bcrypt] python-multipart

# Run server
uvicorn 02_fastapi_basics:app --reload

# Access interactive docs at http://localhost:8000/docs
```

---

## 🤖 Phase 6: Machine Learning

### ML Basics (`phase6-ml/01_ml_basics.py`)
**What you'll learn:**
- Data preprocessing
- Train/test split
- Classification models
- Regression models
- Model evaluation
- Feature importance
- Model persistence (save/load)

**Setup & Run:**
```bash
# Install dependencies
pip install numpy pandas matplotlib seaborn scikit-learn joblib

# Run
python code-examples/phase6-ml/01_ml_basics.py
```

### ML Web Integration (`phase6-ml/02_ml_web_integration.py`)
**What you'll learn:**
- Serving ML models with FastAPI
- Creating prediction endpoints
- Input validation with Pydantic
- Batch predictions
- Model versioning
- Health checks
- Production-ready ML API

**Setup & Run:**
```bash
# Install dependencies
pip install fastapi uvicorn scikit-learn joblib numpy pandas

# Run
uvicorn 02_ml_web_integration:app --reload

# Access at http://localhost:8000/docs
```

**Test it:**
```bash
# Make prediction
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
  }'
```

---

## 🎓 Practice Exercises

### Python Exercises (`exercises/python_exercises.py`)
**Exercises included:**
1. Sum of list
2. Print even numbers
3. Book dictionary
4. Prime number checker
5. Car class
6. **Bonus:** Fibonacci, palindrome, word counter, temperature converter, shopping cart

**Run it:**
```bash
python code-examples/exercises/python_exercises.py
```

### JavaScript Exercises (`exercises/javascript_exercises.js`)
**Exercises included:**
1. Find largest number
2. Reverse string
3. Book object with methods
4. Array to uppercase
5. Car class
6. **Bonus:** FizzBuzz, remove duplicates, count vowels, todo list manager

**Run it:**
```bash
node code-examples/exercises/javascript_exercises.js
```

---

## 💡 Learning Tips

### 1. **Start Simple**
Begin with Phase 1 foundations before moving to advanced topics.

### 2. **Type Along**
Don't just read—type out the code yourself to build muscle memory.

### 3. **Experiment**
Modify the examples to see what happens. Break things and fix them!

### 4. **Complete Exercises**
Practice exercises are crucial for reinforcing concepts.

### 5. **Build Projects**
Use these examples as building blocks for your own projects.

### 6. **Use Debuggers**
Learn to use debugging tools in your IDE or browser.

### 7. **Read Error Messages**
Error messages tell you what's wrong—read them carefully!

---

## 🚀 Quick Start Guide

### For Complete Beginners:
```bash
# 1. Start with Python basics
python code-examples/phase1-foundations/01_python_basics.py

# 2. Move to JavaScript basics
node code-examples/phase1-foundations/02_javascript_basics.js

# 3. Practice exercises
python code-examples/exercises/python_exercises.py
node code-examples/exercises/javascript_exercises.js

# 4. Try HTML/CSS (open in browser)
open code-examples/phase2-frontend/01_html_css_basics.html
```

### For Intermediate Learners:
```bash
# 1. Backend development
node code-examples/phase3-backend/01_express_api_basics.js
# or
uvicorn 02_fastapi_basics:app --reload

# 2. React application
# Set up React app and use 02_react_todo_app.jsx

# 3. Machine Learning
python code-examples/phase6-ml/01_ml_basics.py
python code-examples/phase6-ml/02_ml_web_integration.py
```

---

## 📖 Code Explanation Format

Each code file follows this structure:

```python
"""
FILE HEADER
- What you'll learn
- Topics covered
"""

# ============================================
# SECTION 1: TOPIC NAME
# ============================================

# Code with inline comments
# Explaining each concept

# Example usage
# Expected output

# ============================================
# SECTION 2: NEXT TOPIC
# ============================================

# ... and so on
```

---

## 🔗 Related Resources

### Main Documentation
- `../README.md` - Complete roadmap
- `../TASK_CHECKLIST.md` - Track your progress
- `../PROJECT_IDEAS.md` - Build real projects
- `../LEARNING_SCHEDULE.md` - Study plans
- `../RESOURCES.md` - Learning resources

### Online Resources
- **Python Docs:** https://docs.python.org/
- **JavaScript MDN:** https://developer.mozilla.org/
- **React Docs:** https://react.dev/
- **FastAPI Docs:** https://fastapi.tiangolo.com/
- **Scikit-learn Docs:** https://scikit-learn.org/

---

## ❓ Common Issues & Solutions

### Issue: Module not found
**Solution:** Install required packages
```bash
pip install <package_name>
# or
npm install <package_name>
```

### Issue: Port already in use
**Solution:** Use different port or kill existing process
```bash
# Kill process on port 3000
lsof -ti:3000 | xargs kill -9

# Or use different port
PORT=3001 node server.js
```

### Issue: Permission denied
**Solution:** Check file permissions or use sudo (carefully)
```bash
chmod +x script.sh
# or
sudo pip install package_name
```

---

## 🎯 Next Steps

After completing these examples:

1. ✅ **Build a complete project** combining multiple concepts
2. ✅ **Deploy your application** to the cloud
3. ✅ **Add advanced features** (authentication, real database, etc.)
4. ✅ **Contribute to open source** projects
5. ✅ **Build your portfolio** with real projects

---

## 💬 Need Help?

- 📚 Read the comments in code files—they explain everything
- 🔍 Google error messages—they're your friend
- 💬 Ask in communities (Stack Overflow, Reddit, Discord)
- 📖 Check official documentation
- 🎥 Watch tutorial videos for visual learning

---

## 📝 Notes

- All code examples are **self-contained** and **runnable**
- Examples include **production best practices**
- Code is **heavily commented** for learning
- **Error handling** is included in examples
- Examples progress from **simple to complex**

---

**🎉 Happy Coding! Keep building and learning!**

