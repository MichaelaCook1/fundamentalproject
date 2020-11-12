from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os import getenv

app = Flask(__name__)

app.config['SQLAlCHEMY_DATABASE_URI'] = getenv('DB_URI')
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from application import routes
