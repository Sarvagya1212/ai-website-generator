import React, { useState } from 'react';
import axios from 'axios';
import CodePreview from '../components/CodePreview';

function Generator() {
    const [prompt, setPrompt] = useState('');
    const [loading, setLoading] = useState(false);
    const [generatedCode, setGeneratedCode] = useState(null);

    const handleGenerate = async () => {
        if (!prompt.trim()) return;

        setLoading(true);
        try {
            // Updated URL to match Flask backend default port 5000
            const response = await axios.post('http://localhost:5000/api/generate', {
                prompt: prompt
            });
            setGeneratedCode(response.data.code);
        } catch (error) {
            console.error('Generation failed:', error);
            alert('Generation failed. Please ensure the backend is running.');
        }
        setLoading(false);
    };

    return (
        <div className="container mx-auto p-6">
            <h1 className="text-3xl font-bold mb-6">AI Website Generator</h1>

            <textarea
                className="w-full p-4 border rounded-lg mb-4"
                rows="4"
                placeholder="Describe your website... (e.g., 'Create a portfolio website for a photographer with a dark theme')"
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
            />

            <button
                onClick={handleGenerate}
                disabled={loading}
                className="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 disabled:bg-blue-400"
            >
                {loading ? 'Generating...' : 'Generate Website'}
            </button>

            {generatedCode && (
                <CodePreview code={generatedCode} />
            )}
        </div>
    );
}

export default Generator;
