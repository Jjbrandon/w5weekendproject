from flask import render_template, redirect, request, url_for, request, Blueprint
from werkzeug import datastructures
from .forms import LoginForm, UserInfoForm
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

from app.models import User, db

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate():
        username = form.username.data
        password = form.password.data
        remember_me = form.remember_me.data


        user=User.query.filter_by(username=username).first()

        if user is None or not check_password_hash(user.password, password):
            return redirect(url_for('auth.login'))

        login_user(user, remember = remember_me)
        print(current_user)
        return redirect(url_for('home'))

    return render_template('login.html', title='Sign In', form=form)



@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    my_form = UserInfoForm()
    if request.method == 'POST':
        if my_form.validate():

            username = my_form.username.data
            email = my_form.email.data
            password = my_form.password.data

            user = User(username, email, password)
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('home'))
    
    else:
        print('Not validated, dummy!')
    return render_template('signup.html', form=my_form)


@auth.route('/logout')
def logmeout():
    logout_user()
    return redirect(url_for('auth.login'))