import re

class CodeParser:
    @staticmethod
    def extract_html(generated_text):
        html_match = re.search(r'HTML:(.*?)(?:CSS:|$)', generated_text, re.DOTALL)
        return html_match.group(1).strip() if html_match else ""
    
    @staticmethod
    def extract_css(generated_text):
        css_match = re.search(r'CSS:(.*?)(?:JS:|$)', generated_text, re.DOTALL)
        return css_match.group(1).strip() if css_match else ""
    
    @staticmethod
    def extract_js(generated_text):
        js_match = re.search(r'JS:(.*?)$', generated_text, re.DOTALL)
        return js_match.group(1).strip() if js_match else ""
