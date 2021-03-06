from app import SQLAlchemy
from sqlalchemy.sql import func
db = SQLAlchemy()


class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.String(100), primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    budgets = db.relationship('Budget', backref='customer', lazy=True)
    purchases = db.relationship('Purchase', backref='customer', lazy=True)
    items = db.relationship('Item', backref='customer', lazy=True)

    backref = db.backref('Customer', lazy='joined')

    def __init__(self, client_id, first_name, last_name, email):
        self.id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }


class Budget(db.Model):
    __tablename__ = 'budget'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(100), db.ForeignKey(
        'customer.id'), nullable=False)
    budget = db.Column(db.Float(), nullable=False)
    category = db.Column(db.String(100))
    date = db.Column(db.DateTime(), server_default=func.now())

    def __init__(self, customer_id, budget, category):
        self.customer_id = customer_id
        self.budget = budget
        self.category = category

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'budget': self.budget,
            'category': self.category,
            'date': self.date
        }

    def serialize_list(l):
        return [m.serialize() for m in l]


class Purchase(db.Model):
    __tablename__ = 'purchase'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(100), db.ForeignKey(
        'customer.id'), nullable=False)
    total_amount = db.Column(db.Float(), nullable=False)
    date = db.Column(db.DateTime(), server_default=func.now())
    items = db.relationship('Item', backref='purchase', lazy=True)
    backref = db.backref('Purchase', lazy='joined')

    def __init__(self, customer_id, total_amount):
        self.customer_id = customer_id
        self.total_amount = total_amount

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'total_amount': self.total_amount,
            'date': self.date,
        }

    def serialize_list(l):
        return [m.serialize() for m in l]


class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    purchase_id = db.Column(db.Integer, db.ForeignKey(
        'purchase.id'), nullable=False)
    customer_id = db.Column(db.String(100), db.ForeignKey(
        'customer.id'), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    category = db.Column(db.String(100))
    name = db.Column(db.Text())
    date = db.Column(db.DateTime(), server_default=func.now())

    def __init__(self, customer_id, purchase_id, price, category, name):
        self.customer_id = customer_id
        self.purchase_id = purchase_id
        self.price = price
        self.category = category
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'purchase_id': self.purchase_id,
            'price': self.price,
            'category': self.category,
            'name': self.name,
            'date': self.date,
        }
    def serialize_list(l):
        return [m.serialize() for m in l]
