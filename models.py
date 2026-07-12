"""
Models placeholder: database backend removed.

These classes are lightweight containers kept for compatibility
with imports elsewhere. Data is provided by `data.py`.
"""
from types import SimpleNamespace


class _Model(SimpleNamespace):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class User(_Model):
    pass


class Course(_Model):
    pass


class Booking(_Model):
    pass


class Testimonial(_Model):
    pass


class BlogPost(_Model):
    pass


class ContactMessage(_Model):
    pass


class FAQ(_Model):
    pass


class GalleryImage(_Model):
    pass


class Service(_Model):
    pass


class TeamMember(_Model):
    pass
