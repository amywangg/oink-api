from app import db

class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.String(100), primary_key=True)
    first_name = db.Column(db.String(50),nullable=False )
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    budgets = db.relationship('budget', backref='customer', lazy=True)
    purchases = db.relationship('purchase', backref='customer', lazy=True)
        backref=db.backref('purchase', lazy='joined'))

    def __init__(self, name, author, published):
        self.id = id
        self.author = author 
        self.published = published

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email':self.email
        } 

class Budget(db.Model):
    __tablename__ = 'budget'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(100),db.ForeignKey('customer.id'),nullable=False)
    budget = db.Column(db.Float(),nullable=False)
    category = db.Column(db.String(100))
    date = db.Column(db.DateTime())

    def __init__(self, name, author, published):
        self.id = id
        self.customer_id = customer_id
        self.budget = budget
        self.category = category
        self.date = date

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'customer_id': self.customer_id,
            'budget': self.budget,
            'category':self.category,
            'date':self.date
        }

class Purchase(db.Model):
    __tablename__ = 'purchase'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(100),db.ForeignKey('customer.id'),nullable=False)
    total_amount = db.Column(db.Float(),nullable=False)
    date = db.Column(db.DateTime())
    items = db.relationship('item', backref='purchase', lazy=True)
        backref=db.backref('purchase', lazy='joined'))

    def __init__(self, name, author, published):
        self.id = id
        self.customer_id = customer_id
        self.total_amount = total_amount
        self.date = date

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id, 
            'customer_id': self.customer_id,
            'total_amount': self.total_amount,
            'date': self.date,
        }

class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    purchase_id = db.Column(db.Integer,db.ForeignKey('purchase.id'),nullable=False)
    price = db.Column(db.Float(),nullable=False)
    category = db.Column(db.String(100))
    date = db.Column(db.DateTime())
    
    def __init__(self, name, author, published):
        self.id = id
        self.purchase_id = purchase_id
        self.price = price
        self.category = category
        self.date = date

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id, 
            'purchase_id': self.purchase_id,
            'price': self.price,
            'category':self.category,
            'date':self.date,
        }

