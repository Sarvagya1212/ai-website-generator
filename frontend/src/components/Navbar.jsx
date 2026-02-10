import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
    return (
        <nav className="bg-gray-800 text-white p-4">
            <div className="container mx-auto flex justify-between items-center">
                <Link to="/" className="text-xl font-bold">AI Website Generator</Link>
                <div className="space-x-4">
                    <Link to="/" className="hover:text-gray-300">Generator</Link>
                    {/* Add more links here later like Projects */}
                </div>
            </div>
        </nav>
    );
}

export default Navbar;
