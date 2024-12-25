import React, { Component } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './components/Dashboard/Dashboard';
import Note from './components/Note/Note';
import './static/dashboard.css';

function App() {
    return (
        <Router>
            <Routes>
                <Route path='/' element={<Dashboard />} />
                <Route path='/note' element={<Note />} />
            </Routes>
        </Router>
    );
}

export default App;
