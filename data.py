from types import SimpleNamespace

# In-memory fixtures to replace the database-driven models.
COURSES = [
    SimpleNamespace(id=1, title='Information Technology', category='IT', duration='6 Weeks', requirements='Basic computer literacy', learning_outcomes='Gain foundational IT skills', certification='Certificate of Completion', overview='A hands-on introduction to modern IT operations.', featured=True, published=True),
    SimpleNamespace(id=2, title='Networking', category='Networking', duration='8 Weeks', requirements='Basic networking awareness', learning_outcomes='Configure and troubleshoot networks', certification='Networking Certificate', overview='Deep dive into network administration and troubleshooting.', featured=True, published=True),
    SimpleNamespace(id=3, title='Cybersecurity', category='Security', duration='8 Weeks', requirements='Basic IT knowledge', learning_outcomes='Protect systems against threats', certification='Security Certificate', overview='Modern cybersecurity practices for professionals.', featured=True, published=True),
]

SERVICES = [
    SimpleNamespace(id=1, name='Computer Repair', description='Reliable repair and maintenance services', icon='bi-tools', published=True),
    SimpleNamespace(id=2, name='Corporate Training', description='Tailored employee training programs', icon='bi-people', published=True),
    SimpleNamespace(id=3, name='Computer Sales', description='Enterprise-grade workstation solutions', icon='bi-laptop', published=True),
]

TESTIMONIALS = [
    SimpleNamespace(id=1, author='Alicia M.', role='Operations Lead', content='The training transformed our team.', published=True),
    SimpleNamespace(id=2, author='David T.', role='IT Manager', content='Professional, engaging, and highly relevant.', published=True),
]

BLOG_POSTS = [
    SimpleNamespace(id=1, title='How to Prepare Your Team for Cloud Adoption', slug='cloud-adoption', content='Cloud skills are essential for every modern organization.', published=True),
    SimpleNamespace(id=2, title='Top Cybersecurity Habits for Remote Teams', slug='cybersecurity-habits', content='Protect your team with practical habits and tools.', published=True),
]

FAQS = [
    SimpleNamespace(id=1, question='Do you offer on-site training?', answer='Yes, we provide both on-site and remote training.', published=True),
    SimpleNamespace(id=2, question='Can you support corporate clients?', answer='Absolutely. We tailor programs for businesses of all sizes.', published=True),
]

GALLERY = [
    SimpleNamespace(id=1, title='Training Session', image_url='/static/images/hero.jpg', published=True),
    SimpleNamespace(id=2, title='Repair Service', image_url='/static/images/hero.jpg', published=True),
]

TEAM = [
    SimpleNamespace(id=1, name='Mina Johnson', role='Lead Instructor', bio='Experienced trainer in IT and leadership.', published=True),
    SimpleNamespace(id=2, name='Carlos Reed', role='Technical Specialist', bio='Specializes in networking and support.', published=True),
]

USERS = []
