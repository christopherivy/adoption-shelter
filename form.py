from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField

# PETER  - In this area, how would I know that I need to import these elements?
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional, DataRequired


# these are the input fields for the form
class AddPetForm(FlaskForm):
    # age_range = range(1, 50)

    # this is the name of the pet
    name = StringField('Pet Name', validators=[InputRequired()])
    
    # gender = SelectField("Gender", choices = [('male', 'Male'), ('female', 'Female')])

    # this is going to be a dropdown list of pets
    species = SelectField('Species',
    choices = [('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])

    # this is a link that user provides
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    
    # this is going to be a number field
    age = IntegerField('Age', validators = [Optional(), NumberRange(min = 0, max = 30)])
    
    # text area info about pet
    notes = TextAreaField('Comments', validators=[Optional(), Length(min=10)])


class EditPetForm(FlaskForm):
    """ Use this to edit and existing pet. """

    name = StringField('Name', validators=[Optional()])

    # update the photo
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])

    notes = StringField('Notes', validators=[Optional(), Length(min=10)])

    available = BooleanField('Available?')