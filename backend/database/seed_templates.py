"""Seed the templates table with component variants."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from models import SessionLocal, Base, engine, Template

TEMPLATES = [
    # ── Navbars (3) ───────────────────────────────────────────────────────
    {
        "name": "Minimal Navbar",
        "category": "navbar",
        "html_template": '<nav class="nav-minimal"><div class="nav-container"><a href="#" class="logo">Brand</a><ul class="nav-links"><li><a href="#">Home</a></li><li><a href="#">About</a></li><li><a href="#">Contact</a></li></ul></div></nav>',
        "css_template": ".nav-minimal{background:#fff;padding:1rem 2rem;box-shadow:0 2px 10px rgba(0,0,0,.06)}.nav-container{max-width:1200px;margin:0 auto;display:flex;justify-content:space-between;align-items:center}.logo{font-size:1.4rem;font-weight:700;color:#333}.nav-links{display:flex;list-style:none;gap:2rem}.nav-links a{color:#555;font-weight:500;text-decoration:none;transition:color .3s}.nav-links a:hover{color:#6c63ff}",
        "js_template": "",
    },
    {
        "name": "Mega Menu Navbar",
        "category": "navbar",
        "html_template": '<nav class="nav-mega"><div class="nav-container"><a href="#" class="logo">Brand</a><ul class="nav-links"><li class="has-dropdown"><a href="#">Products</a><div class="mega-dropdown"><div class="mega-col"><h4>Category A</h4><a href="#">Item 1</a><a href="#">Item 2</a></div><div class="mega-col"><h4>Category B</h4><a href="#">Item 3</a><a href="#">Item 4</a></div></div></li><li><a href="#">Pricing</a></li></ul></div></nav>',
        "css_template": ".nav-mega{background:#1a1a2e;padding:1rem 2rem}.nav-container{max-width:1200px;margin:0 auto;display:flex;justify-content:space-between;align-items:center}.logo{color:#fff;font-size:1.4rem;font-weight:700}.nav-links{display:flex;list-style:none;gap:2rem}.nav-links a{color:#ccc;text-decoration:none;transition:color .3s}.nav-links a:hover{color:#6c63ff}.has-dropdown{position:relative}.mega-dropdown{display:none;position:absolute;top:100%;left:0;background:#16213e;border-radius:12px;padding:1.5rem;min-width:300px;gap:2rem}.has-dropdown:hover .mega-dropdown{display:flex}.mega-col h4{color:#6c63ff;margin-bottom:.5rem}.mega-col a{display:block;padding:.25rem 0;color:#aaa;font-size:.9rem}",
        "js_template": "",
    },
    {
        "name": "Sidebar Navigation",
        "category": "navbar",
        "html_template": '<aside class="sidebar"><div class="sidebar-header"><span class="logo">Brand</span></div><ul class="sidebar-links"><li><a href="#">🏠 Home</a></li><li><a href="#">📊 Dashboard</a></li><li><a href="#">⚙️ Settings</a></li><li><a href="#">📁 Projects</a></li></ul></aside>',
        "css_template": ".sidebar{position:fixed;left:0;top:0;width:240px;height:100vh;background:#0f0f1a;padding:2rem 1rem;display:flex;flex-direction:column;gap:2rem}.sidebar-header .logo{color:#fff;font-size:1.3rem;font-weight:700}.sidebar-links{list-style:none;display:flex;flex-direction:column;gap:.5rem}.sidebar-links a{color:#888;text-decoration:none;padding:.75rem 1rem;border-radius:10px;transition:all .3s;display:block}.sidebar-links a:hover{background:#1a1a2e;color:#fff}",
        "js_template": "",
    },
    # ── Heroes (5) ────────────────────────────────────────────────────────
    {
        "name": "Split Hero",
        "category": "hero",
        "html_template": '<section class="hero-split"><div class="hero-text"><h1>Build Something <span>Amazing</span></h1><p>Create stunning websites with the power of AI.</p><a href="#" class="btn">Get Started</a></div><div class="hero-image"><div class="placeholder-img"></div></div></section>',
        "css_template": ".hero-split{display:flex;align-items:center;min-height:100vh;padding:4rem;gap:4rem}.hero-text{flex:1}.hero-text h1{font-size:3.5rem;line-height:1.1;margin-bottom:1rem}.hero-text span{background:linear-gradient(135deg,#6c63ff,#ff6584);-webkit-background-clip:text;-webkit-text-fill-color:transparent}.hero-text p{font-size:1.2rem;color:#666;margin-bottom:2rem}.btn{background:#6c63ff;color:#fff;padding:.9rem 2rem;border-radius:50px;text-decoration:none;font-weight:600}.hero-image{flex:1;display:flex;justify-content:center}.placeholder-img{width:100%;max-width:450px;aspect-ratio:4/3;background:linear-gradient(135deg,#6c63ff22,#ff658422);border-radius:20px}",
        "js_template": "",
    },
    {
        "name": "Centered Hero",
        "category": "hero",
        "html_template": '<section class="hero-centered"><h1>Welcome to the <span>Future</span></h1><p>AI-powered solutions for modern businesses</p><div class="hero-btns"><a href="#" class="btn-primary">Start Free</a><a href="#" class="btn-ghost">Learn More</a></div></section>',
        "css_template": ".hero-centered{min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:2rem}.hero-centered h1{font-size:4rem;margin-bottom:1rem}.hero-centered span{color:#6c63ff}.hero-centered p{font-size:1.3rem;color:#777;margin-bottom:2.5rem}.hero-btns{display:flex;gap:1rem}.btn-primary{background:#6c63ff;color:#fff;padding:.85rem 2rem;border-radius:50px;text-decoration:none;font-weight:600}.btn-ghost{border:2px solid #6c63ff;color:#6c63ff;padding:.85rem 2rem;border-radius:50px;text-decoration:none;font-weight:600}",
        "js_template": "",
    },
    {
        "name": "Video Background Hero",
        "category": "hero",
        "html_template": '<section class="hero-video"><div class="overlay"></div><div class="hero-content"><h1>Immersive Experiences</h1><p>Engage your audience with cinematic design</p><a href="#" class="btn">Explore</a></div></section>',
        "css_template": ".hero-video{position:relative;min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;background:#111}.overlay{position:absolute;inset:0;background:rgba(0,0,0,.6)}.hero-content{position:relative;z-index:1;color:#fff}.hero-content h1{font-size:3.5rem;margin-bottom:1rem}.hero-content p{font-size:1.2rem;opacity:.8;margin-bottom:2rem}.btn{background:#6c63ff;color:#fff;padding:.85rem 2rem;border-radius:50px;text-decoration:none;font-weight:600}",
        "js_template": "",
    },
    {
        "name": "Gradient Hero",
        "category": "hero",
        "html_template": '<section class="hero-gradient"><h1>Transform Your Ideas</h1><p>From concept to reality in seconds</p><a href="#" class="btn">Try Now</a></section>',
        "css_template": ".hero-gradient{min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;background:linear-gradient(135deg,#0f0c29,#302b63,#24243e);color:#fff;padding:2rem}.hero-gradient h1{font-size:4rem;margin-bottom:1rem}.hero-gradient p{font-size:1.2rem;opacity:.7;margin-bottom:2rem}.btn{background:linear-gradient(135deg,#6c63ff,#ff6584);color:#fff;padding:.85rem 2rem;border-radius:50px;text-decoration:none;font-weight:600}",
        "js_template": "",
    },
    {
        "name": "Animated Particles Hero",
        "category": "hero",
        "html_template": '<section class="hero-animated" id="heroAnimated"><canvas id="particleCanvas"></canvas><div class="hero-content"><h1>Innovation Starts Here</h1><p>Powered by next-gen technology</p><a href="#" class="btn">Discover</a></div></section>',
        "css_template": ".hero-animated{position:relative;min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;background:#0a0a1a;color:#fff;overflow:hidden}#particleCanvas{position:absolute;inset:0;z-index:0}.hero-content{position:relative;z-index:1}.hero-content h1{font-size:3.5rem;margin-bottom:1rem}.hero-content p{opacity:.7;font-size:1.2rem;margin-bottom:2rem}.btn{background:#6c63ff;color:#fff;padding:.85rem 2rem;border-radius:50px;text-decoration:none;font-weight:600}",
        "js_template": "const c=document.getElementById('particleCanvas');if(c){const x=c.getContext('2d');c.width=window.innerWidth;c.height=window.innerHeight;const p=Array.from({length:80},()=>({x:Math.random()*c.width,y:Math.random()*c.height,r:Math.random()*2+1,dx:(Math.random()-.5)*.5,dy:(Math.random()-.5)*.5}));(function d(){x.clearRect(0,0,c.width,c.height);p.forEach(i=>{i.x+=i.dx;i.y+=i.dy;if(i.x<0||i.x>c.width)i.dx*=-1;if(i.y<0||i.y>c.height)i.dy*=-1;x.beginPath();x.arc(i.x,i.y,i.r,0,Math.PI*2);x.fillStyle='rgba(108,99,255,0.5)';x.fill()});requestAnimationFrame(d)})()}",
    },
    # ── Contact Forms (2) ─────────────────────────────────────────────────
    {
        "name": "Floating Label Form",
        "category": "form",
        "html_template": '<form class="form-floating"><div class="field"><input type="text" id="name" required /><label for="name">Your Name</label></div><div class="field"><input type="email" id="email" required /><label for="email">Email</label></div><div class="field"><textarea id="msg" rows="4" required></textarea><label for="msg">Message</label></div><button type="submit" class="btn">Send</button></form>',
        "css_template": ".form-floating{max-width:480px;margin:0 auto;display:flex;flex-direction:column;gap:1.5rem}.field{position:relative}.field input,.field textarea{width:100%;padding:1rem;border:1px solid #ddd;border-radius:10px;font-size:1rem;background:transparent}.field label{position:absolute;left:1rem;top:1rem;color:#999;transition:all .2s;pointer-events:none}.field input:focus+label,.field input:valid+label,.field textarea:focus+label,.field textarea:valid+label{top:-.6rem;left:.7rem;font-size:.75rem;background:#fff;padding:0 .3rem;color:#6c63ff}.field input:focus,.field textarea:focus{border-color:#6c63ff;outline:none}.btn{background:#6c63ff;color:#fff;padding:.85rem;border:none;border-radius:50px;font-size:1rem;font-weight:600;cursor:pointer}",
        "js_template": "",
    },
    {
        "name": "Multi-Step Form",
        "category": "form",
        "html_template": '<div class="multistep-form"><div class="steps"><span class="step active">1</span><span class="step">2</span><span class="step">3</span></div><div class="step-content active" data-step="1"><h3>Personal Info</h3><input type="text" placeholder="Full Name" /><input type="email" placeholder="Email" /><button class="btn next-btn">Next</button></div><div class="step-content" data-step="2"><h3>Your Project</h3><textarea placeholder="Describe your project" rows="4"></textarea><button class="btn next-btn">Next</button></div><div class="step-content" data-step="3"><h3>Confirm</h3><p>Ready to submit?</p><button class="btn">Submit</button></div></div>',
        "css_template": ".multistep-form{max-width:480px;margin:0 auto}.steps{display:flex;justify-content:center;gap:1rem;margin-bottom:2rem}.step{width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:#eee;font-weight:600}.step.active{background:#6c63ff;color:#fff}.step-content{display:none;flex-direction:column;gap:1rem}.step-content.active{display:flex}.step-content input,.step-content textarea{padding:.9rem;border:1px solid #ddd;border-radius:10px;font-size:1rem}.btn{background:#6c63ff;color:#fff;padding:.85rem;border:none;border-radius:50px;font-size:1rem;cursor:pointer}",
        "js_template": "document.querySelectorAll('.next-btn').forEach(b=>{b.addEventListener('click',()=>{const cur=b.closest('.step-content');const next=cur.nextElementSibling;if(next&&next.classList.contains('step-content')){cur.classList.remove('active');next.classList.add('active');const steps=document.querySelectorAll('.step');steps.forEach((s,i)=>{s.classList.toggle('active',i<=Array.from(document.querySelectorAll('.step-content')).indexOf(next))})}})});",
    },
    # ── Galleries (3) ─────────────────────────────────────────────────────
    {
        "name": "Masonry Gallery",
        "category": "gallery",
        "html_template": '<div class="masonry"><div class="masonry-item" style="background:#6c63ff33;height:250px"></div><div class="masonry-item" style="background:#ff658433;height:320px"></div><div class="masonry-item" style="background:#43e97b33;height:200px"></div><div class="masonry-item" style="background:#f5af1933;height:280px"></div><div class="masonry-item" style="background:#6c63ff33;height:350px"></div><div class="masonry-item" style="background:#ff658433;height:220px"></div></div>',
        "css_template": ".masonry{columns:3;gap:1rem;padding:2rem}.masonry-item{break-inside:avoid;border-radius:12px;margin-bottom:1rem;transition:transform .3s}.masonry-item:hover{transform:scale(1.03)}@media(max-width:768px){.masonry{columns:2}}@media(max-width:480px){.masonry{columns:1}}",
        "js_template": "",
    },
    {
        "name": "Carousel Gallery",
        "category": "gallery",
        "html_template": '<div class="carousel-wrap"><button class="car-btn prev">&#10094;</button><div class="carousel-track"><div class="car-slide active" style="background:#6c63ff44"></div><div class="car-slide" style="background:#ff658444"></div><div class="car-slide" style="background:#43e97b44"></div></div><button class="car-btn next">&#10095;</button></div>',
        "css_template": ".carousel-wrap{position:relative;max-width:800px;margin:0 auto;overflow:hidden;border-radius:16px}.carousel-track{display:flex;transition:transform .5s}.car-slide{min-width:100%;height:400px}.car-btn{position:absolute;top:50%;transform:translateY(-50%);background:rgba(0,0,0,.4);color:#fff;border:none;font-size:1.5rem;padding:.75rem 1rem;cursor:pointer;z-index:1;border-radius:50%}.prev{left:1rem}.next{right:1rem}",
        "js_template": "let idx=0;const slides=document.querySelectorAll('.car-slide');const track=document.querySelector('.carousel-track');document.querySelector('.next')?.addEventListener('click',()=>{idx=(idx+1)%slides.length;track.style.transform=`translateX(-${idx*100}%)`});document.querySelector('.prev')?.addEventListener('click',()=>{idx=(idx-1+slides.length)%slides.length;track.style.transform=`translateX(-${idx*100}%)`});",
    },
    {
        "name": "Lightbox Grid Gallery",
        "category": "gallery",
        "html_template": '<div class="grid-gallery"><div class="grid-item" style="background:#6c63ff33" onclick="openLightbox(this)"></div><div class="grid-item" style="background:#ff658433" onclick="openLightbox(this)"></div><div class="grid-item" style="background:#43e97b33" onclick="openLightbox(this)"></div><div class="grid-item" style="background:#f5af1933" onclick="openLightbox(this)"></div></div><div class="lightbox" id="lightbox" onclick="closeLightbox()"><div class="lb-content"></div></div>',
        "css_template": ".grid-gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:1rem;padding:2rem}.grid-item{height:220px;border-radius:12px;cursor:pointer;transition:transform .3s}.grid-item:hover{transform:scale(1.05)}.lightbox{display:none;position:fixed;inset:0;background:rgba(0,0,0,.85);z-index:1000;align-items:center;justify-content:center}.lightbox.open{display:flex}.lb-content{width:70%;height:70%;border-radius:16px}",
        "js_template": "function openLightbox(el){const lb=document.getElementById('lightbox');lb.querySelector('.lb-content').style.background=el.style.background;lb.classList.add('open')}function closeLightbox(){document.getElementById('lightbox').classList.remove('open')}",
    },
    # ── Footers (3) ───────────────────────────────────────────────────────
    {
        "name": "Multi-Column Footer",
        "category": "footer",
        "html_template": '<footer class="footer-multi"><div class="footer-grid"><div class="footer-col"><h4>Brand</h4><p>Building the future, one pixel at a time.</p></div><div class="footer-col"><h4>Links</h4><a href="#">Home</a><a href="#">About</a><a href="#">Services</a></div><div class="footer-col"><h4>Contact</h4><a href="#">hello@brand.com</a><a href="#">Twitter</a></div></div><div class="footer-bottom"><p>&copy; 2026 Brand. All rights reserved.</p></div></footer>',
        "css_template": ".footer-multi{background:#0f0f1a;color:#aaa;padding:4rem 2rem 1.5rem}.footer-grid{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:2rem}.footer-col h4{color:#fff;margin-bottom:1rem}.footer-col a{display:block;color:#888;text-decoration:none;padding:.25rem 0;transition:color .3s}.footer-col a:hover{color:#6c63ff}.footer-bottom{text-align:center;margin-top:3rem;padding-top:1.5rem;border-top:1px solid #1a1a2e;font-size:.85rem}",
        "js_template": "",
    },
    {
        "name": "Minimal Footer",
        "category": "footer",
        "html_template": '<footer class="footer-minimal"><p>&copy; 2026 Brand &middot; <a href="#">Privacy</a> &middot; <a href="#">Terms</a></p></footer>',
        "css_template": ".footer-minimal{padding:2rem;text-align:center;color:#888;font-size:.9rem}.footer-minimal a{color:#6c63ff;text-decoration:none}",
        "js_template": "",
    },
    {
        "name": "Mega Footer",
        "category": "footer",
        "html_template": '<footer class="footer-mega"><div class="footer-top"><div class="footer-brand"><h3>Brand</h3><p>Empowering creativity with technology</p></div><form class="newsletter"><input type="email" placeholder="Your email" /><button type="submit">Subscribe</button></form></div><div class="footer-cols"><div><h4>Product</h4><a href="#">Features</a><a href="#">Pricing</a><a href="#">API</a></div><div><h4>Company</h4><a href="#">About</a><a href="#">Careers</a><a href="#">Blog</a></div><div><h4>Support</h4><a href="#">Help Center</a><a href="#">Docs</a><a href="#">Status</a></div></div><div class="footer-bar"><p>&copy; 2026 Brand</p></div></footer>',
        "css_template": ".footer-mega{background:#0a0a1a;color:#aaa;padding:4rem 2rem 1rem}.footer-top{max-width:1100px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:2rem;margin-bottom:3rem}.footer-brand h3{color:#fff;margin-bottom:.5rem}.newsletter{display:flex;gap:.5rem}.newsletter input{padding:.7rem 1rem;border:1px solid #333;border-radius:50px;background:transparent;color:#fff;min-width:220px}.newsletter button{background:#6c63ff;color:#fff;border:none;padding:.7rem 1.5rem;border-radius:50px;cursor:pointer}.footer-cols{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:repeat(3,1fr);gap:2rem;margin-bottom:3rem}.footer-cols h4{color:#fff;margin-bottom:1rem}.footer-cols a{display:block;color:#777;text-decoration:none;padding:.2rem 0;transition:color .3s}.footer-cols a:hover{color:#6c63ff}.footer-bar{text-align:center;padding-top:1.5rem;border-top:1px solid #1a1a2e;font-size:.85rem}",
        "js_template": "",
    },
    # ── Cards (4) ─────────────────────────────────────────────────────────
    {
        "name": "Product Card",
        "category": "card",
        "html_template": '<div class="product-card"><div class="card-img" style="background:#6c63ff22"></div><div class="card-body"><span class="badge">New</span><h3>Product Name</h3><p class="price">$99.00</p><button class="btn">Add to Cart</button></div></div>',
        "css_template": ".product-card{max-width:320px;border-radius:16px;overflow:hidden;background:#fff;box-shadow:0 10px 40px rgba(0,0,0,.08);transition:transform .3s}.product-card:hover{transform:translateY(-5px)}.card-img{height:200px}.card-body{padding:1.5rem}.badge{background:#6c63ff;color:#fff;padding:.25rem .75rem;border-radius:50px;font-size:.75rem;font-weight:600}.card-body h3{margin:.75rem 0 .5rem}.price{font-size:1.3rem;font-weight:700;color:#6c63ff;margin-bottom:1rem}.btn{width:100%;padding:.75rem;border:none;background:#6c63ff;color:#fff;border-radius:50px;font-weight:600;cursor:pointer}",
        "js_template": "",
    },
    {
        "name": "Profile Card",
        "category": "card",
        "html_template": '<div class="profile-card"><div class="avatar" style="background:#6c63ff44"></div><h3>Jane Doe</h3><p class="role">Product Designer</p><div class="stats"><div><strong>142</strong><span>Projects</span></div><div><strong>8.5k</strong><span>Followers</span></div></div><button class="btn">Follow</button></div>',
        "css_template": ".profile-card{max-width:300px;text-align:center;padding:2.5rem 2rem;border-radius:20px;background:#fff;box-shadow:0 10px 40px rgba(0,0,0,.08)}.avatar{width:80px;height:80px;border-radius:50%;margin:0 auto 1rem}.role{color:#888;margin-bottom:1.5rem}.stats{display:flex;justify-content:center;gap:2rem;margin-bottom:1.5rem}.stats div{display:flex;flex-direction:column}.stats strong{font-size:1.1rem}.stats span{font-size:.8rem;color:#999}.btn{padding:.7rem 2rem;border:none;background:#6c63ff;color:#fff;border-radius:50px;cursor:pointer;font-weight:600}",
        "js_template": "",
    },
    {
        "name": "Pricing Card",
        "category": "card",
        "html_template": '<div class="pricing-card"><span class="plan-name">Pro</span><div class="plan-price"><span class="currency">$</span><span class="amount">49</span><span class="period">/mo</span></div><ul class="features"><li>✓ Unlimited projects</li><li>✓ Priority support</li><li>✓ Custom domains</li><li>✓ Analytics</li></ul><button class="btn">Get Started</button></div>',
        "css_template": ".pricing-card{max-width:320px;padding:3rem 2rem;border-radius:20px;background:linear-gradient(135deg,#1a1a2e,#16213e);color:#fff;text-align:center}.plan-name{background:#6c63ff;padding:.3rem 1rem;border-radius:50px;font-size:.85rem;font-weight:600}.plan-price{margin:1.5rem 0}.currency{font-size:1.5rem;vertical-align:super}.amount{font-size:3.5rem;font-weight:700}.period{color:#888}.features{list-style:none;text-align:left;margin:2rem 0}.features li{padding:.5rem 0;color:#ccc;border-bottom:1px solid #ffffff0a}.btn{width:100%;padding:.85rem;border:none;background:#6c63ff;color:#fff;border-radius:50px;font-size:1rem;font-weight:600;cursor:pointer}",
        "js_template": "",
    },
    {
        "name": "Feature Card",
        "category": "card",
        "html_template": '<div class="feature-card"><div class="icon-wrap">⚡</div><h3>Lightning Fast</h3><p>Optimized for speed and performance. Your websites load in milliseconds.</p></div>',
        "css_template": ".feature-card{max-width:320px;padding:2rem;border-radius:16px;background:#fff;border:1px solid #eee;transition:all .3s}.feature-card:hover{border-color:#6c63ff;box-shadow:0 15px 50px rgba(108,99,255,.12)}.icon-wrap{width:50px;height:50px;background:#6c63ff11;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:1.5rem;margin-bottom:1rem}.feature-card h3{margin-bottom:.5rem}.feature-card p{color:#777;font-size:.95rem;line-height:1.6}",
        "js_template": "",
    },
]


def seed():
    """Insert all templates if the table is empty."""
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if db.query(Template).count() == 0:
            for t in TEMPLATES:
                db.add(Template(**t))
            db.commit()
            print(f"✓ Seeded {len(TEMPLATES)} templates.")
        else:
            print("Templates already seeded, skipping.")
    finally:
        db.close()


if __name__ == '__main__':
    seed()
