from flask import Flask, request, url_for, redirect, jsonify, Blueprint, json
from app import SQLAlchemy
db = SQLAlchemy()

budget = Blueprint('budget', __name__)


@budget.route("/create", methods=['POST'])
def create_budget():
    return 'Success'
