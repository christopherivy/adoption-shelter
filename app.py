# REQUIRED BELOW-------------------------------------

# //PETER // In the solution it mentions url_for and jsonify. How would I know that I need to use those?
from flask import (
    Flask,
    url_for,
    render_template,
    redirect,
    flash,
    jsonify,
)

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from form import AddPetForm, EditPetForm

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pets_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "chickenzarecool21837"
# app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
# debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

# PETER why do I need this toolbar here?
# toolbar = DebugToolbarExtension(app)

# REQUIRED ABOVE-------------------------------------


# this is the home page
@app.route("/")
def list_pets():
   """List of the Pets"""

   pets = Pet.query.all()
   return render_template("pet_list.html", pets=pets)


# this is to add a pet page
@app.route('/add', methods = ['GET', 'POST'])
def add_pet():
    """ Add a pet """

    form = AddPetForm()

    # // Ask Peter to explain this section a little more.
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != 'csrf_token'}
        new_pet = Pet(**data)

        db.session.add(new_pet)
        db.session.commit()
        flash(f'{new_pet.name} added.')
        return redirect(url_for('list_pets'))

    else:
        return render_template('pet_add_form.html', form=form)
    

# this route is for the individual pet by id
@app.route('/<int:pet_id>', methods = ['GET', 'POST'])
def edit_pet(pet_id):
    """ Edit Pet """

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet) # Ask Peter about this (obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.notes = form.notes.data #Ask Peter what is .data. Where coming from.
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f'{pet.name} updated.')
        return redirect(url_for('list_pets'))

    else:
        return render_template('pet_edit_form.html', form=form, pet=pet)







@app.route('/api/pets/<int:pet_id>', methods=['GET'])
def api_get_pet(pet_id):
    """ Return basic information about the pet in JSON """

    pet = Pet.query.get_or_404(pet_id)
    info = {'name': pet.name, 'age': pet.age}

    return jsonify(info)