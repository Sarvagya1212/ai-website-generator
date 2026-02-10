import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Generator from './pages/Generator';

function App() {
    return (
        <Router>
            <div className="min-h-screen bg-gray-50 text-gray-900">
                <Navbar />
                <Routes>
                    <Route path="/" element={<Generator />} />
                    {/* Add more routes here */}
                </Routes>
            </div>
        </Router>
    );
}

export default App;
