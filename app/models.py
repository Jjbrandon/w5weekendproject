

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(256), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)


class PostHero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=False)
    superpower = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500))
    comics_appeared_in = db.Column(db.Numeric())
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, name, image, superpower, description, comics_appeared_in, user_id):
        self.name = name 
        self.superpower = superpower
        self.image = image
        self.description = description
        self.comics_appeared_in = comics_appeared_in
        self.user_id = user_id



    