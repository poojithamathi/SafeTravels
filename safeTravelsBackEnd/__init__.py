import flask
from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from os import path
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from redis import Redis

safeTravelsdb = SQLAlchemy()
dbName = "safeTravels.db"
redis = Redis()

def safeTravels():
    safeTravel = Flask(__name__)

    safeTravel.config["SESSION_PERMANENT"]=False

    safeTravel.config["SECRET_KEY"] = "NishadGupta"
    safeTravel.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{dbName}'
    safeTravelsdb.init_app(safeTravel)
    # flask.session.clear()


    from .models.paths import paths
    from .models.auth import auth
    from .models.payment import payment

    safeTravel.register_blueprint(paths, url_prefix = "/")
    safeTravel.register_blueprint(auth, url_prefix = "/")
    safeTravel.register_blueprint(payment, url_prefix = "/")


    from .models.dbModels import User, Note, passwordQuestions, paymentQuestions, wishlistHotels, wishlistRestaurants
    createDatabase(safeTravel)

    return safeTravel


def createDatabase(safeTravel):
    if not path.exists('safeTravelsBackEnd/' + dbName):
        with safeTravel.app_context():
            safeTravelsdb.create_all()
            safeTravelsdb.session.commit()
        print("Database Successfully Created")


