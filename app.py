from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask(__name__)
cors=CORS(app)
if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(__file__), 'database'))):
    os.makedirs(os.path.normpath(os.path.join(os.path.dirname(__file__), 'database')))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.normpath(os.path.join(os.path.dirname(__file__), 'database/app.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)