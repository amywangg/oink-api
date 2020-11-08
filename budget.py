from flask import Flask, request, url_for, redirect, jsonify, Blueprint, json
from models import Budget
from app import SQLAlchemy
db = SQLAlchemy()

budget = Blueprint('budget', __name__)


@budget.route("/create", methods=['POST'])
def createBudget():
    if request.method == 'POST':
        params = request.json
        category = params['category']
        budget = int(params['amount'])
        customer_id = params['client_id']

    try:
        budget = Budget(
            customer_id,
            budget,
            category,
        )
        db.session.add(budget)
        db.session.commit()
        return "Budget added"
    except Exception as e:
        return(str(e))


@budget.route("/<budget_id>", methods=['GET'])
def getBudget(budget_id):
    try:
        budget = Budget.query.filter_by(id=budget_id).first()
        return jsonify(budget.serialize())
    except Exception as e:
        return(str(e))
