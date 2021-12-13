from flask import render_template, redirect, request, url_for, request, Blueprint
from werkzeug import datastructures
from app import app, db
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

from app.models import User

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
