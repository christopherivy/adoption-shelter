# ASSIGNMENT-----------------------------------------
# REQUIRED BELOW-------------------------------------

from flask_sqlalchemy import SQLAlchemy

DEFAULT_PET_IMAGE = 'https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif'

db = SQLAlchemy()

# REQUIRED ABOVE-------------------------------------


class Pet(db.Model):
    """Pet Model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.Text,nullable=False)  
    species = db.Column(db.Text,nullable=False)  
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """ Return image for a pet """

        return self.photo_url or DEFAULT_PET_IMAGE

def connect_db(app): # // why is this at the bottom of this assignment was at the top of others.
    db.app = app
    db.init_app(app)
