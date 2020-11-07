 from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import secrets

secret_key = secret.token_hex(16)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:root@35.246.122.101'
app.config["SECRET_KEY"] ='its a secret'

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)
app = Flask(__name__) 

if __name__ == '__main__':
app.run(host=”0.0.0.0”,debug=True)

