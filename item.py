from flask import Flask, request, url_for, redirect, jsonify, Blueprint, json
from models import Purchase, Item
from app import SQLAlchemy
from sqlalchemy.sql import select
db = SQLAlchemy()

item = Blueprint('item', __name__)


@item.route("/create", methods=['POST'])
def createItem():
    if request.method == 'POST':
        params = request.json
        customer_id = params['client_id']
        purchase_id = int(params['purchase_id'])
        price = float(params['price'])
        # category = params['category']
        category = 'general'
        name = params['name']

    try:
        item = Item(
            customer_id,
            purchase_id,
            price,
            category,
            name
        )
        db.session.add(item)
        db.session.commit()
        return "item added"
    except Exception as e:
        return(str(e))


@item.route("/<item_id>", methods=['GET'])
def getItem(item_id):
    try:
        item = Item.query.filter_by(id=item_id).first()
        return jsonify(item.serialize())
    except Exception as e:
        return(str(e))


@item.route("/purchase/<purchase_id>", methods=['GET'])
def getPurchaseItems(purchase_id):
    try:
        items = Item.query.select().where(purchase_id=purchase_id)
        return jsonify(items.serialize())
    except Exception as e:
        return(str(e))


@item.route("/user/<customer_id>", methods=['GET'])
def getAllItems(customer_id):
    try:
        items = Item.query.select().where(customer_id=customer_id)
        return jsonify(items.serialize())
    except Exception as e:
        return(str(e))
