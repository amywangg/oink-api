# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from flask_cors import CORS
from customer import customer
from budget import budget
from item import item
from purchase import purchase

import os

app = Flask(__name__)
# register blueprint routes
app.register_blueprint(customer, url_prefix='/user')
app.register_blueprint(budget, url_prefix='/budget')
app.register_blueprint(item, url_prefix='/item')
app.register_blueprint(purchase, url_prefix='/purchase')

# allow for cross origin requests
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
from models import Customer, Budget, Purchase, Item


# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)