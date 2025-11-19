/**
 * EXPRESS.JS REST API - COMPLETE EXAMPLE
 * Learn backend development with Node.js and Express
 * 
 * Topics covered:
 * - Express setup
 * - Routing
 * - Middleware
 * - CRUD operations
 * - Error handling
 * - Validation
 * - Authentication basics
 */

const express = require('express');
const cors = require('cors');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');

// ============================================
// APP SETUP
// ============================================

const app = express();
const PORT = process.env.PORT || 3000;
const SECRET_KEY = 'your-secret-key-change-in-production';

// Middleware
app.use(express.json()); // Parse JSON bodies
app.use(cors()); // Enable CORS

// In-memory data store (use database in production)
let users = [];
let todos = [];
let nextUserId = 1;
let nextTodoId = 1;

// ============================================
// MIDDLEWARE EXAMPLES
// ============================================

// Logging middleware
const loggerMiddleware = (req, res, next) => {
    const timestamp = new Date().toISOString();
    console.log(`[${timestamp}] ${req.method} ${req.url}`);
    next(); // Pass control to next middleware
};

// Authentication middleware
const authMiddleware = (req, res, next) => {
    try {
        // Get token from header
        const token = req.headers.authorization?.split(' ')[1]; // Bearer TOKEN
        
        if (!token) {
            return res.status(401).json({ error: 'No token provided' });
        }
        
        // Verify token
        const decoded = jwt.verify(token, SECRET_KEY);
        req.userId = decoded.userId; // Add userId to request
        next();
    } catch (error) {
        res.status(401).json({ error: 'Invalid token' });
    }
};

// Apply logger middleware to all routes
app.use(loggerMiddleware);

// ============================================
// AUTHENTICATION ROUTES
// ============================================

/**
 * POST /api/auth/register
 * Register a new user
 */
app.post('/api/auth/register', async (req, res) => {
    try {
        const { username, email, password } = req.body;
        
        // Validation
        if (!username || !email || !password) {
            return res.status(400).json({ 
                error: 'All fields are required' 
            });
        }
        
        if (password.length < 6) {
            return res.status(400).json({ 
                error: 'Password must be at least 6 characters' 
            });
        }
        
        // Check if user exists
        if (users.find(u => u.email === email)) {
            return res.status(400).json({ 
                error: 'User already exists' 
            });
        }
        
        // Hash password
        const hashedPassword = await bcrypt.hash(password, 10);
        
        // Create user
        const user = {
            id: nextUserId++,
            username,
            email,
            password: hashedPassword,
            createdAt: new Date().toISOString()
        };
        
        users.push(user);
        
        // Generate token
        const token = jwt.sign({ userId: user.id }, SECRET_KEY, { expiresIn: '7d' });
        
        // Return user (without password) and token
        const { password: _, ...userWithoutPassword } = user;
        res.status(201).json({ 
            user: userWithoutPassword, 
            token 
        });
        
    } catch (error) {
        res.status(500).json({ error: 'Server error' });
    }
});

/**
 * POST /api/auth/login
 * Login existing user
 */
app.post('/api/auth/login', async (req, res) => {
    try {
        const { email, password } = req.body;
        
        // Validation
        if (!email || !password) {
            return res.status(400).json({ 
                error: 'Email and password are required' 
            });
        }
        
        // Find user
        const user = users.find(u => u.email === email);
        if (!user) {
            return res.status(401).json({ 
                error: 'Invalid credentials' 
            });
        }
        
        // Check password
        const isValidPassword = await bcrypt.compare(password, user.password);
        if (!isValidPassword) {
            return res.status(401).json({ 
                error: 'Invalid credentials' 
            });
        }
        
        // Generate token
        const token = jwt.sign({ userId: user.id }, SECRET_KEY, { expiresIn: '7d' });
        
        // Return user and token
        const { password: _, ...userWithoutPassword } = user;
        res.json({ 
            user: userWithoutPassword, 
            token 
        });
        
    } catch (error) {
        res.status(500).json({ error: 'Server error' });
    }
});

/**
 * GET /api/auth/me
 * Get current user (requires authentication)
 */
app.get('/api/auth/me', authMiddleware, (req, res) => {
    const user = users.find(u => u.id === req.userId);
    if (!user) {
        return res.status(404).json({ error: 'User not found' });
    }
    
    const { password: _, ...userWithoutPassword } = user;
    res.json(userWithoutPassword);
});

// ============================================
// TODO CRUD ROUTES (Protected)
// ============================================

/**
 * GET /api/todos
 * Get all todos for current user
 */
app.get('/api/todos', authMiddleware, (req, res) => {
    const userTodos = todos.filter(todo => todo.userId === req.userId);
    res.json(userTodos);
});

/**
 * GET /api/todos/:id
 * Get a specific todo
 */
app.get('/api/todos/:id', authMiddleware, (req, res) => {
    const todoId = parseInt(req.params.id);
    const todo = todos.find(t => t.id === todoId && t.userId === req.userId);
    
    if (!todo) {
        return res.status(404).json({ error: 'Todo not found' });
    }
    
    res.json(todo);
});

/**
 * POST /api/todos
 * Create a new todo
 */
app.post('/api/todos', authMiddleware, (req, res) => {
    const { title, description } = req.body;
    
    // Validation
    if (!title || title.trim() === '') {
        return res.status(400).json({ error: 'Title is required' });
    }
    
    const todo = {
        id: nextTodoId++,
        userId: req.userId,
        title: title.trim(),
        description: description || '',
        completed: false,
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString()
    };
    
    todos.push(todo);
    res.status(201).json(todo);
});

/**
 * PUT /api/todos/:id
 * Update a todo
 */
app.put('/api/todos/:id', authMiddleware, (req, res) => {
    const todoId = parseInt(req.params.id);
    const { title, description, completed } = req.body;
    
    const todoIndex = todos.findIndex(t => t.id === todoId && t.userId === req.userId);
    
    if (todoIndex === -1) {
        return res.status(404).json({ error: 'Todo not found' });
    }
    
    // Update todo
    if (title !== undefined) todos[todoIndex].title = title.trim();
    if (description !== undefined) todos[todoIndex].description = description;
    if (completed !== undefined) todos[todoIndex].completed = completed;
    todos[todoIndex].updatedAt = new Date().toISOString();
    
    res.json(todos[todoIndex]);
});

/**
 * DELETE /api/todos/:id
 * Delete a todo
 */
app.delete('/api/todos/:id', authMiddleware, (req, res) => {
    const todoId = parseInt(req.params.id);
    const todoIndex = todos.findIndex(t => t.id === todoId && t.userId === req.userId);
    
    if (todoIndex === -1) {
        return res.status(404).json({ error: 'Todo not found' });
    }
    
    const deletedTodo = todos.splice(todoIndex, 1)[0];
    res.json({ message: 'Todo deleted', todo: deletedTodo });
});

/**
 * PATCH /api/todos/:id/toggle
 * Toggle todo completion
 */
app.patch('/api/todos/:id/toggle', authMiddleware, (req, res) => {
    const todoId = parseInt(req.params.id);
    const todoIndex = todos.findIndex(t => t.id === todoId && t.userId === req.userId);
    
    if (todoIndex === -1) {
        return res.status(404).json({ error: 'Todo not found' });
    }
    
    todos[todoIndex].completed = !todos[todoIndex].completed;
    todos[todoIndex].updatedAt = new Date().toISOString();
    
    res.json(todos[todoIndex]);
});

// ============================================
// PUBLIC ROUTES
// ============================================

/**
 * GET /
 * Root endpoint
 */
app.get('/', (req, res) => {
    res.json({
        message: 'Todo API Server',
        version: '1.0.0',
        endpoints: {
            auth: {
                register: 'POST /api/auth/register',
                login: 'POST /api/auth/login',
                me: 'GET /api/auth/me'
            },
            todos: {
                list: 'GET /api/todos',
                get: 'GET /api/todos/:id',
                create: 'POST /api/todos',
                update: 'PUT /api/todos/:id',
                delete: 'DELETE /api/todos/:id',
                toggle: 'PATCH /api/todos/:id/toggle'
            }
        }
    });
});

/**
 * GET /api/health
 * Health check endpoint
 */
app.get('/api/health', (req, res) => {
    res.json({
        status: 'OK',
        timestamp: new Date().toISOString(),
        users: users.length,
        todos: todos.length
    });
});

// ============================================
// ERROR HANDLING
// ============================================

// 404 handler
app.use((req, res) => {
    res.status(404).json({ error: 'Endpoint not found' });
});

// Global error handler
app.use((err, req, res, next) => {
    console.error('Error:', err);
    res.status(500).json({ 
        error: 'Internal server error',
        message: err.message 
    });
});

// ============================================
// START SERVER
// ============================================

app.listen(PORT, () => {
    console.log(`\n${'='.repeat(50)}`);
    console.log(`🚀 Server running on http://localhost:${PORT}`);
    console.log(`${'='.repeat(50)}\n`);
    console.log('Available endpoints:');
    console.log(`  📖 GET  ${`http://localhost:${PORT}/`}`);
    console.log(`  💚 GET  ${`http://localhost:${PORT}/api/health`}`);
    console.log(`  🔐 POST ${`http://localhost:${PORT}/api/auth/register`}`);
    console.log(`  🔐 POST ${`http://localhost:${PORT}/api/auth/login`}`);
    console.log(`  📝 GET  ${`http://localhost:${PORT}/api/todos`}`);
    console.log(`\n${'='.repeat(50)}\n`);
});

/*
 * ============================================
 * TO RUN THIS SERVER:
 * ============================================
 * 
 * 1. Install dependencies:
 *    npm init -y
 *    npm install express cors jsonwebtoken bcrypt
 * 
 * 2. Run server:
 *    node 01_express_api_basics.js
 * 
 * 3. Test with curl or Postman:
 * 
 *    # Register
 *    curl -X POST http://localhost:3000/api/auth/register \
 *      -H "Content-Type: application/json" \
 *      -d '{"username":"john","email":"john@example.com","password":"password123"}'
 * 
 *    # Login (copy the token from response)
 *    curl -X POST http://localhost:3000/api/auth/login \
 *      -H "Content-Type: application/json" \
 *      -d '{"email":"john@example.com","password":"password123"}'
 * 
 *    # Create todo (replace YOUR_TOKEN)
 *    curl -X POST http://localhost:3000/api/todos \
 *      -H "Content-Type: application/json" \
 *      -H "Authorization: Bearer YOUR_TOKEN" \
 *      -d '{"title":"Learn Express","description":"Build REST API"}'
 * 
 *    # Get todos
 *    curl http://localhost:3000/api/todos \
 *      -H "Authorization: Bearer YOUR_TOKEN"
 * 
 * ============================================
 * LEARNING NOTES:
 * ============================================
 * 
 * 1. EXPRESS BASICS:
 *    - app.get(), app.post(), app.put(), app.delete()
 *    - Route parameters: req.params
 *    - Query strings: req.query
 *    - Request body: req.body
 * 
 * 2. MIDDLEWARE:
 *    - Functions that run before route handlers
 *    - Can modify req/res objects
 *    - Call next() to continue
 * 
 * 3. AUTHENTICATION:
 *    - JWT tokens for stateless auth
 *    - bcrypt for password hashing
 *    - Authorization header
 * 
 * 4. ERROR HANDLING:
 *    - Try-catch blocks
 *    - HTTP status codes
 *    - Global error handler
 * 
 * 5. REST API DESIGN:
 *    - GET: Read
 *    - POST: Create
 *    - PUT: Update (full)
 *    - PATCH: Update (partial)
 *    - DELETE: Remove
 * 
 * ============================================
 * NEXT STEPS:
 * ============================================
 * 
 * 1. Connect to real database (MongoDB, PostgreSQL)
 * 2. Add input validation library (Joi, express-validator)
 * 3. Add rate limiting
 * 4. Add request validation
 * 5. Add API documentation (Swagger)
 * 6. Add tests (Jest, Supertest)
 * 7. Add logging (Winston, Morgan)
 */

