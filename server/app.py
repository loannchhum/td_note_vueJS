import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask( __name__ )
app.config['SECRET_KEY'] = 'test'
cors=CORS(app, ressources={r"/quiz/api/v1.0/questionnaire/*":{"origins": "*"}})
if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(__file__), '../database'))):
    os.makedirs(os.path.normpath(os.path.join(os.path.dirname(__file__), '../database')))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.normpath(os.path.join(os.path.dirname(__file__), '../database/app.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

