from flask import Flask, request, url_for, redirect, jsonify, Blueprint, json
from app import SQLAlchemy
from models import Customer

db = SQLAlchemy()

customer = Blueprint('customer', ___name___)

@customer.route("/signup", methods=['POST'])
def signup():
    first_name=request.args.get('first_name')
    last_name=request.args.get('last_name')
    email=request.args.get('email')
    client_id=request.args.get('client_id')

    try:
        customer=Customer(
            id=client_id
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        db.session.add(customer)
        db.session.commit()
        return "Customer added. Customer id={}".format(customer.id)
    except Exception as e:
	    return(str(e))

@app.route("/login/<client_id>")
def login(client_id):
    try:
        customer=Customer.query.filter_by(id=client_id).first()
        return jsonify(customer.serialize())
    except Exception as e:
	    return(str(e))