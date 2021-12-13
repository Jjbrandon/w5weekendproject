from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


from .models import User, db

###### bringing in routes for registration #######
from .auth.routes import auth
from .hero.routes import hero



app = Flask(__name__)
app.config.from_object(Config)
migrate = Migrate(app,db)

from app import routes, models, auth, hero

from .models import User, PostHero, db

login = LoginManager()


db.init_app(app)
login.init_app(app)

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

app.register_blueprint(auth)
app.register_blueprint(hero)