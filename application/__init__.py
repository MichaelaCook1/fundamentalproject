from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets

secret_key = secrets.token_hex(16)
app = Flask(__name__)

app.config['SQLAlCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@35.242.191.104"
app.config['SECRET_KEY'] = "its a secret"
db = SQLAlchemy(app)

from application import routes
