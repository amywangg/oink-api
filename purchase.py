from flask import Flask, request, url_for, redirect, jsonify, Blueprint, json
from models import Purchase
from app import SQLAlchemy
from sqlalchemy.sql import select

db = SQLAlchemy()

purchase = Blueprint('purchase', __name__)


@purchase.route("/create", methods=['POST'])
def createPurchase():
    if request.method == 'POST':
        params = request.json
        total_amount = float(params['amount'])
        customer_id = params['client_id']

    try:
        purchase = Purchase(
            customer_id,
            total_amount,
        )
        db.session.add(purchase)
        db.session.commit()
        return str(purchase.id)
    except Exception as e:
        return(str(e))


@purchase.route("/<purchase_id>", methods=['GET'])
def getPurchase(purchase_id):
    try:
        purchase = Purchase.query.filter_by(id=purchase_id).first()
        return jsonify(purchase.serialize())
    except Exception as e:
        return(str(e))

@purchase.route("/user/<customer_id>", methods=['GET'])
def getAllPurchases(customer_id):
    try:
        purchases = Purchase.query.select().where(customer_id=customer_id)
        return jsonify(purchases.serialize())
    except Exception as e:
        return(str(e))