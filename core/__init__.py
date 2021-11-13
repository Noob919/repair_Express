from flask import Flask
from flask_sqlalchemy import SQLAlchemy
 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/RepairExpress'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = '4d7f399067323b1b9d0272bd'

db = SQLAlchemy(app)

from core import routes