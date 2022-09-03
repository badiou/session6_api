import os
from sqlalchemy import Column, String, Integer, Boolean, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os
#python3 -m venv venv          et    venv\Scripts\activate
#psql -h localhost -p 5432 -U postgres -d session6_db -f plants_database.sql ceci est la commande pour exécuter vers la base de données
#pg_dump -h localhost -p 5432 -U postgres -d session6_db > db_base.sql
###################################################################################################################
#
#                                       HERE I HAVE MAKE M CONNECTION STRING
#
###################################################################################################################
load_dotenv()
PASSWORD=quote_plus(os.getenv("PASSWORD"))
database_name = "db_test"
database_path = "postgresql://{}:{}@{}/{}".format(
    'postgres', PASSWORD, 'localhost:5432', database_name)
db = SQLAlchemy()


# setup_db(app)

###################################################################################################################
#
#
#                                        SET UP MY APPLICATION BY CONNEXION STRING AND MIGRATION
#
###################################################################################################################


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.app = app
    db.init_app(app)
    #db.create_all()  #Cette ligne est décommentée si on souhaite créer automatiquement la base de données au lancement
    # de l'appplication
    migrate = Migrate(app, db)


''' Plant
'''
###################################################################################################################
#
#                                      HERE I HAVE CREATED MY MODEL
#
###################################################################################################################


class Plant(db.Model):
    __tablename__ = 'plants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    scientific_name = Column(String)
    is_poisonous = Column(Boolean)
    primary_color = Column(String)
    state=Column(String,nullable=False)


###################################################################################################################
#
#                                      MY CONSTRUCTOR
#
###################################################################################################################


    def __init__(self, name, scientific_name, is_poisonous, primary_color,state):
        self.name = name
        self.scientific_name = scientific_name
        self.is_poisonous = is_poisonous
        self.primary_color = primary_color
        self.state=state


###################################################################################################################
#
#         I HAVE PERFORM METHOD THAT WILL HELP ME TO INSERT UPDATE OR DELETE
#
###################################################################################################################


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


###################################################################################################################
#
#                 THIS SCRIPT ALLOW ME TO FORMAT A RESPONSE AND PARSE IT INTO JSONIFY LIKE RESPONSE
#
###################################################################################################################


    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'scientific_name': self.scientific_name,
            'is_poisonous': self.is_poisonous,
            'primary_color': self.primary_color,
            'state':self.state
        }
