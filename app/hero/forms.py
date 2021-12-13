from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired 

class CreateHeroForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    superpower = StringField('Power', validators=[DataRequired()])
    image = StringField('Image URL', validators=[DataRequired(),])
    description = StringField('Description')
    comics_appeared_in = IntegerField('Number of Comics')
    submit = SubmitField()