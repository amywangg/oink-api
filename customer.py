from flask import Flask, request, url_for, redirect, jsonify, Blueprint, json
from models import Customer
from app import SQLAlchemy

db = SQLAlchemy()
customer = Blueprint('customer', __name__)


@customer.route("/signup", methods=['POST'])
def createUser():
    if request.method == 'POST':
        params = request.json
        first_name = params['first_name']
        last_name = params['last_name']
        email = params['email']
        client_id = params['id']

    try:
        customer = Customer(
            client_id,
            first_name,
            last_name,
            email
        )
        db.session.add(customer)
        db.session.commit()
        return "Customer added. Customer id={}".format(customer.id)
    except Exception as e:
        return(str(e))


@customer.route("/<client_id>", methods=['GET'])
def getUser(client_id):
    try:
        customer = Customer.query.filter_by(id=client_id).first()
        if customer == None:
            return "null"
        return jsonify(customer.serialize())
    except Exception as e:
        return(str(e))
