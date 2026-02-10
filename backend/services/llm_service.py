import os
import requests
import json
import re


class LLMService:
    """Service for interacting with Hugging Face Inference API to generate websites."""

    SYSTEM_PROMPT = """You are an expert web developer. Given a user's description, generate a complete, 
modern, responsive website. Return ONLY valid code in the following exact format with no other text:

```html
<!-- Your complete HTML here -->
```

```css
/* Your complete CSS here */
```

```javascript
// Your complete JavaScript here
```

Requirements:
- Use modern, semantic HTML5
- Make the design responsive with media queries
- Use a professional color palette
- Include smooth transitions and hover effects
- Use Google Fonts for typography
- Make it visually appealing and production-ready"""

    def __init__(self):
        self.api_token = os.getenv('HF_API_TOKEN', '')
        self.model_id = os.getenv('HF_MODEL_ID', 'meta-llama/Llama-2-7b-chat-hf')
        self.api_url = f"https://api-inference.huggingface.co/models/{self.model_id}"

    def generate_website(self, prompt, template=None):
        """
        Generate website code from a natural language prompt.
        Falls back to a mock response if the API is unavailable.
        """
        # Build the full prompt
        if template:
            full_prompt = (
                f"{self.SYSTEM_PROMPT}\n\n"
                f"Use the following template as a starting point and customize it based on the user's request:\n"
                f"Template HTML:\n{template.get('html_template', '')}\n"
                f"Template CSS:\n{template.get('css_template', '')}\n\n"
                f"User request: {prompt}"
            )
        else:
            full_prompt = f"{self.SYSTEM_PROMPT}\n\nUser request: {prompt}"

        # Try Hugging Face Inference API
        if self.api_token:
            try:
                return self._call_hf_api(full_prompt)
            except Exception as e:
                print(f"HF API error: {e}. Falling back to mock generation.")

        # Fallback: generate a mock website based on the prompt
        return self._generate_mock(prompt)

    def _call_hf_api(self, prompt):
        """Call the Hugging Face Inference API."""
        headers = {"Authorization": f"Bearer {self.api_token}"}
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 2048,
                "temperature": 0.7,
                "top_p": 0.9,
                "return_full_text": False,
            }
        }

        response = requests.post(self.api_url, headers=headers, json=payload, timeout=120)
        response.raise_for_status()

        result = response.json()
        if isinstance(result, list) and len(result) > 0:
            generated_text = result[0].get('generated_text', '')
        else:
            generated_text = str(result)

        return self._parse_code(generated_text)

    def _parse_code(self, raw_text):
        """Extract HTML, CSS, and JS from the LLM's response."""
        html_match = re.search(r'```html\s*(.*?)```', raw_text, re.DOTALL)
        css_match = re.search(r'```css\s*(.*?)```', raw_text, re.DOTALL)
        js_match = re.search(r'```(?:javascript|js)\s*(.*?)```', raw_text, re.DOTALL)

        return {
            'html': html_match.group(1).strip() if html_match else raw_text.strip(),
            'css': css_match.group(1).strip() if css_match else '',
            'js': js_match.group(1).strip() if js_match else '',
        }

    def _generate_mock(self, prompt):
        """Generate a polished mock website when the API is unavailable."""
        # Extract key info from the prompt
        prompt_lower = prompt.lower()
        title = "My Website"
        if 'portfolio' in prompt_lower:
            title = "Portfolio"
        elif 'landing' in prompt_lower:
            title = "Landing Page"
        elif 'blog' in prompt_lower:
            title = "Blog"
        elif 'restaurant' in prompt_lower:
            title = "Restaurant"
        elif 'store' in prompt_lower or 'shop' in prompt_lower:
            title = "Online Store"

        is_dark = 'dark' in prompt_lower

        bg_color = '#0f0f1a' if is_dark else '#ffffff'
        text_color = '#e0e0e0' if is_dark else '#333333'
        accent = '#6c63ff'
        card_bg = '#1a1a2e' if is_dark else '#f8f9fa'

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <a href="#" class="logo">{title}</a>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
            <button class="mobile-toggle" aria-label="Toggle menu">&#9776;</button>
        </div>
    </nav>

    <section id="home" class="hero">
        <div class="hero-content">
            <h1 class="hero-title">Welcome to <span class="gradient-text">{title}</span></h1>
            <p class="hero-subtitle">Built with AI — powered by your imagination</p>
            <div class="hero-buttons">
                <a href="#services" class="btn btn-primary">Explore</a>
                <a href="#contact" class="btn btn-outline">Get in Touch</a>
            </div>
        </div>
        <div class="hero-decoration"></div>
    </section>

    <section id="about" class="section">
        <div class="container">
            <h2 class="section-title">About Us</h2>
            <p class="section-text">We craft beautiful digital experiences that captivate and inspire. Our passion lies in turning ideas into reality through elegant design and powerful technology.</p>
        </div>
    </section>

    <section id="services" class="section section-alt">
        <div class="container">
            <h2 class="section-title">Our Services</h2>
            <div class="cards-grid">
                <div class="card">
                    <div class="card-icon">&#9881;</div>
                    <h3>Web Design</h3>
                    <p>Stunning, responsive designs that look great on any device.</p>
                </div>
                <div class="card">
                    <div class="card-icon">&#9889;</div>
                    <h3>Development</h3>
                    <p>Clean, efficient code built with modern technologies.</p>
                </div>
                <div class="card">
                    <div class="card-icon">&#9734;</div>
                    <h3>Branding</h3>
                    <p>Memorable brand identities that tell your story.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="contact" class="section">
        <div class="container">
            <h2 class="section-title">Contact Us</h2>
            <form class="contact-form" onsubmit="handleSubmit(event)">
                <input type="text" placeholder="Your Name" required />
                <input type="email" placeholder="Your Email" required />
                <textarea placeholder="Your Message" rows="5" required></textarea>
                <button type="submit" class="btn btn-primary">Send Message</button>
            </form>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <p>&copy; 2026 {title}. Generated with AI Website Generator.</p>
        </div>
    </footer>
</body>
</html>"""

        css = f"""/* === Reset & Base === */
*, *::before, *::after {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

body {{
    font-family: 'Inter', sans-serif;
    background-color: {bg_color};
    color: {text_color};
    line-height: 1.6;
    overflow-x: hidden;
}}

a {{
    text-decoration: none;
    color: inherit;
}}

/* === Navbar === */
.navbar {{
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 1000;
    background: {'rgba(15,15,26,0.85)' if is_dark else 'rgba(255,255,255,0.85)'};
    backdrop-filter: blur(12px);
    border-bottom: 1px solid {'rgba(255,255,255,0.08)' if is_dark else 'rgba(0,0,0,0.06)'};
}}

.nav-container {{
    max-width: 1200px;
    margin: 0 auto;
    padding: 1rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}}

.logo {{
    font-size: 1.5rem;
    font-weight: 700;
    background: linear-gradient(135deg, {accent}, #ff6584);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}

.nav-links {{
    display: flex;
    list-style: none;
    gap: 2rem;
}}

.nav-links a {{
    font-weight: 500;
    transition: color 0.3s;
}}

.nav-links a:hover {{
    color: {accent};
}}

.mobile-toggle {{
    display: none;
    background: none;
    border: none;
    color: {text_color};
    font-size: 1.5rem;
    cursor: pointer;
}}

/* === Hero === */
.hero {{
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 6rem 2rem 4rem;
    position: relative;
    overflow: hidden;
}}

.hero-decoration {{
    position: absolute;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, {accent}22, transparent 70%);
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    pointer-events: none;
}}

.hero-title {{
    font-size: clamp(2.5rem, 6vw, 4.5rem);
    font-weight: 700;
    margin-bottom: 1rem;
    position: relative;
    z-index: 1;
}}

.gradient-text {{
    background: linear-gradient(135deg, {accent}, #ff6584, #43e97b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}

.hero-subtitle {{
    font-size: 1.25rem;
    opacity: 0.7;
    margin-bottom: 2.5rem;
    position: relative;
    z-index: 1;
}}

.hero-buttons {{
    display: flex;
    gap: 1rem;
    justify-content: center;
    position: relative;
    z-index: 1;
}}

/* === Buttons === */
.btn {{
    padding: 0.85rem 2rem;
    border-radius: 50px;
    font-weight: 600;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.3s ease;
    border: 2px solid {accent};
    display: inline-block;
}}

.btn-primary {{
    background: {accent};
    color: #fff;
    border-color: {accent};
}}

.btn-primary:hover {{
    background: transparent;
    color: {accent};
    transform: translateY(-2px);
    box-shadow: 0 8px 30px {accent}44;
}}

.btn-outline {{
    background: transparent;
    color: {accent};
}}

.btn-outline:hover {{
    background: {accent};
    color: #fff;
    transform: translateY(-2px);
}}

/* === Sections === */
.section {{
    padding: 6rem 2rem;
}}

.section-alt {{
    background: {card_bg};
}}

.container {{
    max-width: 1100px;
    margin: 0 auto;
}}

.section-title {{
    font-size: 2.2rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 1rem;
}}

.section-text {{
    text-align: center;
    max-width: 650px;
    margin: 0 auto;
    opacity: 0.8;
    font-size: 1.1rem;
}}

/* === Cards === */
.cards-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    margin-top: 3rem;
}}

.card {{
    background: {'#16213e' if is_dark else '#ffffff'};
    border-radius: 16px;
    padding: 2.5rem 2rem;
    text-align: center;
    transition: transform 0.3s, box-shadow 0.3s;
    border: 1px solid {'rgba(255,255,255,0.06)' if is_dark else 'rgba(0,0,0,0.06)'};
}}

.card:hover {{
    transform: translateY(-8px);
    box-shadow: 0 20px 60px {'rgba(108,99,255,0.15)' if is_dark else 'rgba(0,0,0,0.1)'};
}}

.card-icon {{
    font-size: 2.5rem;
    margin-bottom: 1rem;
}}

.card h3 {{
    font-size: 1.3rem;
    margin-bottom: 0.75rem;
}}

.card p {{
    opacity: 0.7;
    font-size: 0.95rem;
}}

/* === Contact Form === */
.contact-form {{
    max-width: 550px;
    margin: 2rem auto 0;
    display: flex;
    flex-direction: column;
    gap: 1rem;
}}

.contact-form input,
.contact-form textarea {{
    padding: 1rem 1.25rem;
    border-radius: 12px;
    border: 1px solid {'rgba(255,255,255,0.12)' if is_dark else 'rgba(0,0,0,0.12)'};
    background: {'#1a1a2e' if is_dark else '#f8f9fa'};
    color: {text_color};
    font-family: inherit;
    font-size: 1rem;
    transition: border-color 0.3s;
}}

.contact-form input:focus,
.contact-form textarea:focus {{
    outline: none;
    border-color: {accent};
}}

/* === Footer === */
.footer {{
    padding: 2rem;
    text-align: center;
    opacity: 0.5;
    font-size: 0.9rem;
    border-top: 1px solid {'rgba(255,255,255,0.06)' if is_dark else 'rgba(0,0,0,0.06)'};
}}

/* === Responsive === */
@media (max-width: 768px) {{
    .nav-links {{
        display: none;
    }}
    .mobile-toggle {{
        display: block;
    }}
    .hero-buttons {{
        flex-direction: column;
        align-items: center;
    }}
}}"""

        js = """// Mobile navigation toggle
document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.querySelector('.mobile-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (toggle) {
        toggle.addEventListener('click', () => {
            navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
            navLinks.style.flexDirection = 'column';
            navLinks.style.position = 'absolute';
            navLinks.style.top = '100%';
            navLinks.style.left = '0';
            navLinks.style.right = '0';
            navLinks.style.padding = '1rem 2rem';
            navLinks.style.background = 'inherit';
        });
    }

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            e.preventDefault();
            const target = document.querySelector(anchor.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // Scroll-triggered fade-in animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.card, .section-title, .section-text').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});

// Contact form handler
function handleSubmit(event) {
    event.preventDefault();
    const btn = event.target.querySelector('button[type="submit"]');
    btn.textContent = 'Sent!';
    btn.style.background = '#43e97b';
    btn.style.borderColor = '#43e97b';
    setTimeout(() => {
        btn.textContent = 'Send Message';
        btn.style.background = '';
        btn.style.borderColor = '';
        event.target.reset();
    }, 2000);
}"""

        return {
            'html': html,
            'css': css,
            'js': js,
        }


# Module-level singleton
llm_service = LLMService()
