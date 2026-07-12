import os
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import current_user
from config import Config
from extensions import login_manager
from routes import register_routes
from data import COURSES, SERVICES, TESTIMONIALS, BLOG_POSTS, FAQS, GALLERY, TEAM

app = Flask(__name__)
app.config.from_object(Config)

login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):
    # No persistent users after DB removal — always return None
    return None

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

register_routes(app)


@app.route('/')
def home():
    featured_courses = [c for c in COURSES if getattr(c, 'featured', False)][:6]
    testimonials = [t for t in TESTIMONIALS if getattr(t, 'published', False)][:3]
    blog_posts = [p for p in BLOG_POSTS if getattr(p, 'published', False)][:3]
    faqs = [f for f in FAQS if getattr(f, 'published', False)][:4]
    services = [s for s in SERVICES if getattr(s, 'published', False)][:6]
    return render_template('index.html', featured_courses=featured_courses, testimonials=testimonials, blog_posts=blog_posts, faqs=faqs, services=services)


@app.route('/about')
def about():
    team = [m for m in TEAM if getattr(m, 'published', False)]
    return render_template('about.html', team=team)


@app.route('/training-programs')
def training_programs():
    courses = [c for c in COURSES if getattr(c, 'published', False)]
    return render_template('training_programs.html', courses=courses)


@app.route('/corporate-training')
def corporate_training():
    return render_template('corporate_training.html')


@app.route('/computer-sales')
def computer_sales():
    return render_template('computer_sales.html')


@app.route('/computer-repairs')
def computer_repairs():
    return render_template('computer_repairs.html')


@app.route('/services')
def services_view():
    services = [s for s in SERVICES if getattr(s, 'published', False)]
    return render_template('services.html', services=services)


@app.route('/gallery')
def gallery():
    images = [g for g in GALLERY if getattr(g, 'published', False)]
    return render_template('gallery.html', images=images)


@app.route('/testimonials')
def testimonials_view():
    items = [t for t in TESTIMONIALS if getattr(t, 'published', False)]
    return render_template('testimonials.html', items=items)


@app.route('/blog')
def blog():
    posts = [p for p in BLOG_POSTS if getattr(p, 'published', False)]
    return render_template('blog.html', posts=posts)


@app.route('/faq')
def faq():
    items = [f for f in FAQS if getattr(f, 'published', False)]
    return render_template('faq.html', items=items)


@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy_policy.html')


@app.route('/terms')
def terms():
    return render_template('terms.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
