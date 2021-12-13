from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_required

from .forms import CreateHeroForm
from app.models import db, PostHero

# create instance of blueprint
hero = Blueprint('hero', __name__, template_folder='hero_templates')

@hero.route('/yourheroes')
@login_required
def yourheroes():
    posts = PostHero.query.filter_by(user_id=current_user.id)
    return render_template('herolist.html', posts = posts)


@hero.route('/createhero', methods = ["GET","POST"])
@login_required
def createhero():
    form = CreateHeroForm()
    if request.method == "POST":
        if form.validate():
            
            name = form.name.data
            image = form.image.data
            superpower = form.superpower.data
            description = form.description.data
            comics_appeared_in = form.comics_appeared_in.data

            # create instance new post
            post = PostHero(name, image, superpower, description, comics_appeared_in, current_user.id)
            # add instance to databse
            db.session.add(post)
            # commit to databse
            db.session.commit()

            return redirect(url_for('hero.createhero'))
    return render_template('createhero.html', form = form)