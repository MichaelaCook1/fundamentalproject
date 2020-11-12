from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@35.246.12.217/board'
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from application import routes
