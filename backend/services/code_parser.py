import re


def parse_generated_code(raw_text):
    """
    Extract HTML, CSS, and JS blocks from raw LLM output.
    Supports fenced code blocks (```html ... ```) and
    falls back to treating the entire output as HTML.
    """
    html = extract_block(raw_text, 'html')
    css = extract_block(raw_text, 'css')
    js = extract_block(raw_text, 'javascript') or extract_block(raw_text, 'js')

    # If no fenced blocks found, treat the whole thing as HTML
    if not html and not css and not js:
        html = raw_text.strip()

    return {
        'html': html,
        'css': css,
        'js': js,
    }


def extract_block(text, language):
    """Extract a fenced code block for the given language."""
    pattern = rf'```{language}\s*(.*?)```'
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else ''


def combine_code(html, css, js):
    """
    Combine separate HTML, CSS, and JS into a single self-contained HTML document.
    Useful for rendering in an iframe preview.
    """
    style_block = f"\n<style>\n{css}\n</style>" if css else ""
    script_block = f"\n<script>\n{js}\n</script>" if js else ""

    # If the HTML already has <head>, inject styles there
    if '<head>' in html.lower():
        combined = html.replace('</head>', f'{style_block}\n</head>')
    else:
        combined = f"{style_block}\n{html}"

    # Inject JS before closing body
    if '</body>' in combined.lower():
        combined = combined.replace('</body>', f'{script_block}\n</body>')
    else:
        combined = f"{combined}{script_block}"

    return combined
