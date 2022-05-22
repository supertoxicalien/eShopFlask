from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fdsaknmnvuqroipcklam knfkla' #encrypt the cookies and session data
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .home import home

    app.register_blueprint(home, url_prefix='/')

    from .models import Item

    create_database(app)

    return app


def create_database(app):
    if not path.exists('shop/' + DB_NAME):
        db.create_all(app=app)
        print('Create DataBase!')
