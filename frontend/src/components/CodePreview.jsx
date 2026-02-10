import React, { useState } from 'react';
import Editor from '@monaco-editor/react';

function CodePreview({ code }) {
    const [activeTab, setActiveTab] = useState('preview');

    return (
        <div className="mt-8 border rounded-lg">
            <div className="flex border-b">
                <button
                    className={`px-4 py-2 ${activeTab === 'preview' ? 'bg-blue-100' : ''}`}
                    onClick={() => setActiveTab('preview')}
                >
                    Preview
                </button>
                <button
                    className={`px-4 py-2 ${activeTab === 'html' ? 'bg-blue-100' : ''}`}
                    onClick={() => setActiveTab('html')}
                >
                    HTML
                </button>
                <button
                    className={`px-4 py-2 ${activeTab === 'css' ? 'bg-blue-100' : ''}`}
                    onClick={() => setActiveTab('css')}
                >
                    CSS
                </button>
            </div>

            <div className="p-4">
                {activeTab === 'preview' && (
                    <iframe
                        title="Website Preview"
                        srcDoc={`${code.html_code}<style>${code.css_code}</style><script>${code.js_code}</script>`}
                        className="w-full h-96 border"
                    />
                )}
                {activeTab === 'html' && (
                    <Editor
                        height="400px"
                        language="html"
                        value={code.html_code}
                        theme="vs-dark"
                    />
                )}
                {activeTab === 'css' && (
                    <Editor
                        height="400px"
                        language="css"
                        value={code.css_code}
                        theme="vs-dark"
                    />
                )}
            </div>
        </div>
    );
}

export default CodePreview;
