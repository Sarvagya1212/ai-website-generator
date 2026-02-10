from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_engine.llama_generator import LlamaWebGenerator
from ai_engine.code_parser import CodeParser
from database.db_manager import DatabaseManager
import os

app = Flask(__name__)
CORS(app)

# Initialize components
llama_gen = LlamaWebGenerator()
db = DatabaseManager()

def analyze_prompt(prompt):
    """Basic analysis of the prompt to determine website type."""
    prompt_lower = prompt.lower()
    if "landing page" in prompt_lower:
        return "landing_page"
    elif "portfolio" in prompt_lower:
        return "portfolio"
    elif "blog" in prompt_lower:
        return "blog"
    elif "ecommerce" in prompt_lower or "shop" in prompt_lower:
        return "ecommerce"
    return "generic"

def parse_and_structure(generated_text):
    """Parse the raw generated text into structured code."""
    return {
        "html_code": CodeParser.extract_html(generated_text),
        "css_code": CodeParser.extract_css(generated_text),
        "js_code": CodeParser.extract_js(generated_text),
        "metadata": {}
    }

@app.route('/api/generate', methods=['POST'])
def generate_website():
    try:
        data = request.json
        user_prompt = data.get('prompt')
        
        if not user_prompt:
            return jsonify({'error': 'Prompt is required'}), 400
        
        # Analyze prompt to determine website type
        website_type = analyze_prompt(user_prompt)
        
        # Generate components
        # Append website type to context to guide generation
        context_prompt = f"Type: {website_type}. {user_prompt}"
        html = llama_gen.generate_code(context_prompt, "full website")
        
        # Parse and structure code
        structured_code = parse_and_structure(html)
        
        # Save to database
        project_id = db.save_project(user_prompt, structured_code)
        
        return jsonify({
            'success': True,
            'project_id': project_id,
            'code': structured_code
        })
    except Exception as e:
        print(f"Error generating website: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/preview/<project_id>', methods=['GET'])
def preview_website(project_id):
    project = db.get_project(project_id)
    if project:
        return jsonify(project)
    return jsonify({'error': 'Project not found'}), 404

@app.route('/api/export/<project_id>', methods=['GET'])
def export_website(project_id):
    # Generate downloadable zip file (placeholder)
    return jsonify({'message': 'Export functionality coming soon'})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
