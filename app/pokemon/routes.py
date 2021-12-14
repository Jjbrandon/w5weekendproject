from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_required

from app.models import db, PostHero, Pokemon
import requests as r

pokemon = Blueprint('pokemon', __name__, template_folder='pokemon_templates')

@pokemon.route('/search/pokemon', methods = ['GET','POST'])
def searchpokemon():
    if request.method == "POST":
        my_pokemon = request.form['poke']
        data = r.get(f'https://pokeapi.co/api/v2/pokemon/{my_pokemon}')
        if data.status_code == 200:
            my_data = data.json()

            pokemon = {
                'name': '',
                'image': '',
                'abilities':[],
                'game_list':[]
            }

            for ability in my_data['abilities']:
                pokemon['abilities'].append(ability['ability']['name'])
            for game in my_data['game_indices']:
                pokemon['game_list'].append(game['version']['name'])
            pokemon['name'] = my_data['name']
            pokemon['image'] = my_data['sprites']['front_default']

            pokemon_name = pokemon['name']
            image = pokemon['image']
            abilities = pokemon['abilities']
            game_list = pokemon['game_list']

            # create instance new post
            post = Pokemon(pokemon_name, image, abilities, game_list)
            # add instance to databse
            db.session.add(post)
            # commit to databse
            db.session.commit()

            return render_template('poke.html', pokemon = pokemon)
        else:
            pokemon = ''
            return render_template('poke.html', pokemon = pokemon)