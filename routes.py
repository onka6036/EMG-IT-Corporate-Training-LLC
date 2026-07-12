from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_required
from forms import RegisterForm, LoginForm, BookingForm
from data import COURSES, SERVICES, TESTIMONIALS, BLOG_POSTS, FAQS, GALLERY, TEAM

bp = Blueprint('main', __name__)


def register_routes(app):
    app.register_blueprint(bp)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            # Authentication disabled after DB removal
            flash('Login unavailable: authentication has been disabled.', 'warning')
        return render_template('auth/login.html', form=form)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            flash('Registration unavailable: account creation is disabled.', 'warning')
        return render_template('auth/register.html', form=form)

    @app.route('/logout')
    @login_required
    def logout():
        flash('Logout unavailable in static mode.', 'info')
        return redirect(url_for('home'))

    @app.route('/student-dashboard')
    @login_required
    def student_dashboard():
        flash('Dashboard unavailable: requires database-backed users.', 'warning')
        return redirect(url_for('home'))

    @app.route('/admin-dashboard')
    @login_required
    def admin_dashboard():
        flash('Admin dashboard unavailable: requires database.', 'warning')
        return redirect(url_for('home'))

    @app.route('/admin/bookings/<int:booking_id>/<status>')
    @login_required
    def update_booking_status(booking_id, status):
        flash('Operation unavailable: booking management requires database.', 'warning')
        return redirect(url_for('admin_dashboard'))

    @app.route('/book-training', methods=['GET', 'POST'])
    def book_training():
        form = BookingForm()
        if form.validate_on_submit():
            flash('Booking received. (Not persisted in static mode)', 'success')
            return redirect(url_for('home'))
        return render_template('book_training.html', form=form)

    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            message = request.form.get('message')
            if name and email and message:
                flash('Thank you for your message. (Not persisted in static mode)', 'success')
                return redirect(url_for('contact'))
            flash('Please fill out the required fields.', 'danger')
        return render_template('contact.html')

    @app.route('/blog/<slug>')
    def blog_post(slug):
        post = next((p for p in BLOG_POSTS if p.slug == slug and getattr(p, 'published', False)), None)
        if not post:
            abort(404)
        return render_template('blog_post.html', post=post)
