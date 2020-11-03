# clientID google api:
# 769564108089-kjitojja4egodmt4n8qor9jj12af2uh4.apps.googleusercontent.com
# client secret:
# ofsJooS741avaDef_-wud46T
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import os

app = Flask(__name__)
# allow for cross origin requests
CORS(app)
# register blueprint routes
app.register_blueprint(customer, url_prefix='/user')
app.register_blueprint(budget, url_prefix='/budget')

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Customer, Budget, Purchase, Item

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)