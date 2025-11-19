/**
 * REACT TODO APP - COMPLETE EXAMPLE
 * Learn React by building a real application
 * 
 * This file demonstrates:
 * - React Components
 * - useState Hook
 * - useEffect Hook
 * - Props
 * - Event Handling
 * - Conditional Rendering
 * - Lists and Keys
 * - Local Storage
 */

import React, { useState, useEffect } from 'react';
import './TodoApp.css'; // Assume CSS file exists

// ============================================
// MAIN APP COMPONENT
// ============================================

function TodoApp() {
    // State management using useState hook
    const [todos, setTodos] = useState([]);
    const [inputValue, setInputValue] = useState('');
    const [filter, setFilter] = useState('all'); // all, active, completed
    const [editingId, setEditingId] = useState(null);
    const [editValue, setEditValue] = useState('');

    // Load todos from localStorage on mount
    useEffect(() => {
        const savedTodos = localStorage.getItem('todos');
        if (savedTodos) {
            setTodos(JSON.parse(savedTodos));
        }
    }, []); // Empty dependency array = run once on mount

    // Save todos to localStorage whenever they change
    useEffect(() => {
        localStorage.setItem('todos', JSON.stringify(todos));
    }, [todos]); // Run when todos changes

    // ============================================
    // HANDLER FUNCTIONS
    // ============================================

    // Add new todo
    const handleAddTodo = (e) => {
        e.preventDefault();
        
        if (inputValue.trim() === '') {
            alert('Please enter a todo!');
            return;
        }

        const newTodo = {
            id: Date.now(),
            text: inputValue.trim(),
            completed: false,
            createdAt: new Date().toISOString()
        };

        setTodos([...todos, newTodo]);
        setInputValue(''); // Clear input
    };

    // Toggle todo completion
    const handleToggle = (id) => {
        setTodos(todos.map(todo =>
            todo.id === id
                ? { ...todo, completed: !todo.completed }
                : todo
        ));
    };

    // Delete todo
    const handleDelete = (id) => {
        if (window.confirm('Are you sure you want to delete this todo?')) {
            setTodos(todos.filter(todo => todo.id !== id));
        }
    };

    // Start editing
    const handleStartEdit = (id, text) => {
        setEditingId(id);
        setEditValue(text);
    };

    // Save edit
    const handleSaveEdit = (id) => {
        if (editValue.trim() === '') {
            alert('Todo cannot be empty!');
            return;
        }

        setTodos(todos.map(todo =>
            todo.id === id
                ? { ...todo, text: editValue.trim() }
                : todo
        ));

        setEditingId(null);
        setEditValue('');
    };

    // Cancel edit
    const handleCancelEdit = () => {
        setEditingId(null);
        setEditValue('');
    };

    // Clear completed todos
    const handleClearCompleted = () => {
        setTodos(todos.filter(todo => !todo.completed));
    };

    // Mark all as completed
    const handleCompleteAll = () => {
        const allCompleted = todos.every(todo => todo.completed);
        setTodos(todos.map(todo => ({ ...todo, completed: !allCompleted })));
    };

    // ============================================
    // COMPUTED VALUES
    // ============================================

    // Filter todos based on current filter
    const filteredTodos = todos.filter(todo => {
        if (filter === 'active') return !todo.completed;
        if (filter === 'completed') return todo.completed;
        return true; // 'all'
    });

    // Statistics
    const totalTodos = todos.length;
    const activeTodos = todos.filter(todo => !todo.completed).length;
    const completedTodos = todos.filter(todo => todo.completed).length;

    // ============================================
    // RENDER
    // ============================================

    return (
        <div className="todo-app">
            <header className="app-header">
                <h1>📝 React Todo App</h1>
                <p>Learn React by building!</p>
            </header>

            {/* Statistics */}
            <div className="stats">
                <div className="stat-item">
                    <span className="stat-number">{totalTodos}</span>
                    <span className="stat-label">Total</span>
                </div>
                <div className="stat-item">
                    <span className="stat-number">{activeTodos}</span>
                    <span className="stat-label">Active</span>
                </div>
                <div className="stat-item">
                    <span className="stat-number">{completedTodos}</span>
                    <span className="stat-label">Completed</span>
                </div>
            </div>

            {/* Add Todo Form */}
            <form onSubmit={handleAddTodo} className="add-todo-form">
                <input
                    type="text"
                    value={inputValue}
                    onChange={(e) => setInputValue(e.target.value)}
                    placeholder="What needs to be done?"
                    className="todo-input"
                />
                <button type="submit" className="btn btn-primary">
                    Add Todo
                </button>
            </form>

            {/* Filter Buttons */}
            <div className="filter-buttons">
                <button
                    className={`btn ${filter === 'all' ? 'btn-active' : ''}`}
                    onClick={() => setFilter('all')}
                >
                    All ({totalTodos})
                </button>
                <button
                    className={`btn ${filter === 'active' ? 'btn-active' : ''}`}
                    onClick={() => setFilter('active')}
                >
                    Active ({activeTodos})
                </button>
                <button
                    className={`btn ${filter === 'completed' ? 'btn-active' : ''}`}
                    onClick={() => setFilter('completed')}
                >
                    Completed ({completedTodos})
                </button>
            </div>

            {/* Bulk Actions */}
            {totalTodos > 0 && (
                <div className="bulk-actions">
                    <button
                        className="btn btn-secondary"
                        onClick={handleCompleteAll}
                    >
                        {todos.every(todo => todo.completed) ? 'Unmark All' : 'Complete All'}
                    </button>
                    {completedTodos > 0 && (
                        <button
                            className="btn btn-danger"
                            onClick={handleClearCompleted}
                        >
                            Clear Completed
                        </button>
                    )}
                </div>
            )}

            {/* Todo List */}
            <div className="todo-list">
                {filteredTodos.length === 0 ? (
                    <div className="empty-state">
                        <p>
                            {filter === 'all' && '🎉 No todos yet. Add one above!'}
                            {filter === 'active' && '✅ No active todos!'}
                            {filter === 'completed' && '📋 No completed todos yet!'}
                        </p>
                    </div>
                ) : (
                    filteredTodos.map(todo => (
                        <TodoItem
                            key={todo.id}
                            todo={todo}
                            isEditing={editingId === todo.id}
                            editValue={editValue}
                            onToggle={handleToggle}
                            onDelete={handleDelete}
                            onStartEdit={handleStartEdit}
                            onSaveEdit={handleSaveEdit}
                            onCancelEdit={handleCancelEdit}
                            onEditChange={setEditValue}
                        />
                    ))
                )}
            </div>
        </div>
    );
}

// ============================================
// TODO ITEM COMPONENT (Child Component)
// ============================================

function TodoItem({
    todo,
    isEditing,
    editValue,
    onToggle,
    onDelete,
    onStartEdit,
    onSaveEdit,
    onCancelEdit,
    onEditChange
}) {
    // If editing this item, show edit form
    if (isEditing) {
        return (
            <div className="todo-item editing">
                <input
                    type="text"
                    value={editValue}
                    onChange={(e) => onEditChange(e.target.value)}
                    className="edit-input"
                    autoFocus
                    onKeyDown={(e) => {
                        if (e.key === 'Enter') onSaveEdit(todo.id);
                        if (e.key === 'Escape') onCancelEdit();
                    }}
                />
                <div className="edit-actions">
                    <button
                        onClick={() => onSaveEdit(todo.id)}
                        className="btn btn-success btn-sm"
                    >
                        ✓ Save
                    </button>
                    <button
                        onClick={onCancelEdit}
                        className="btn btn-secondary btn-sm"
                    >
                        ✗ Cancel
                    </button>
                </div>
            </div>
        );
    }

    // Regular todo item view
    return (
        <div className={`todo-item ${todo.completed ? 'completed' : ''}`}>
            <input
                type="checkbox"
                checked={todo.completed}
                onChange={() => onToggle(todo.id)}
                className="todo-checkbox"
            />
            <span className="todo-text">{todo.text}</span>
            <div className="todo-actions">
                <button
                    onClick={() => onStartEdit(todo.id, todo.text)}
                    className="btn btn-info btn-sm"
                    disabled={todo.completed}
                >
                    ✎ Edit
                </button>
                <button
                    onClick={() => onDelete(todo.id)}
                    className="btn btn-danger btn-sm"
                >
                    🗑 Delete
                </button>
            </div>
        </div>
    );
}

// ============================================
// EXPORT
// ============================================

export default TodoApp;

/*
 * ============================================
 * LEARNING NOTES:
 * ============================================
 * 
 * 1. COMPONENTS:
 *    - TodoApp: Main parent component
 *    - TodoItem: Reusable child component
 * 
 * 2. STATE MANAGEMENT:
 *    - useState: For managing component state
 *    - Multiple state variables for different concerns
 * 
 * 3. SIDE EFFECTS:
 *    - useEffect: For localStorage operations
 *    - Dependency arrays control when effects run
 * 
 * 4. PROPS:
 *    - Pass data and functions from parent to child
 *    - Destructuring props for cleaner code
 * 
 * 5. EVENT HANDLING:
 *    - onClick, onChange, onSubmit
 *    - Arrow functions to pass parameters
 * 
 * 6. CONDITIONAL RENDERING:
 *    - Ternary operators
 *    - && for conditional display
 * 
 * 7. LISTS:
 *    - map() for rendering arrays
 *    - key prop for list items
 * 
 * 8. FORM HANDLING:
 *    - Controlled components
 *    - preventDefault()
 * 
 * ============================================
 * NEXT STEPS:
 * ============================================
 * 
 * 1. Add this CSS file: TodoApp.css
 * 2. Set up React project: npx create-react-app my-app
 * 3. Replace App.js with this code
 * 4. Run: npm start
 * 
 * ENHANCEMENTS TO TRY:
 * - Add due dates
 * - Add categories/tags
 * - Add priority levels
 * - Add search functionality
 * - Add drag-and-drop reordering
 * - Connect to backend API
 */

