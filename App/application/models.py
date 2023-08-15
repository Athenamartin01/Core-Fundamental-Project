from application import app,db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField,SelectField


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_name = db.Column(db.String(30))
    card_no = db.Column(db.String(100))
    card_exp = db.Column(db.String(5))
    cvv = db.Column(db.String(100))
    add_line1 = db.Column(db.String(30))
    add_line2 = db.Column(db.String(30))
    add_line3 = db.Column(db.String(30))
    city = db.Column(db.String(30))
    postcode = db.Column(db.String(8))
    customer = db.relationship('Order',backref="customerbr")

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),unique=True,nullable=False)
    category = db.Column(db.String(30),default="misc")
    price = db.Column(db.Float,nullable=False)
    stock = db.Column(db.Integer,default=0)
    desc = db.Column(db.String(500))
    image = db.Column(db.String(30))
    product = db.relationship('Order_Product',backref='productbr')

class Order(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    is_complete = db.Column(db.Boolean(), default=False)
    date_ordered = db.Column(db.DateTime())
    cust_id = db.Column(db.Integer,db.ForeignKey('customer.id'),nullable=False)
    order = db.relationship('Order_Product',backref='orderbr')

class Order_Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, default=0)
    prod_id = db.Column(db.Integer, db.ForeignKey('product.id'),nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'),nullable=False)
    


class CategoryForm(FlaskForm):
    category =StringField()
    submit = SubmitField('Search')

class Item_to_Basket_Form(FlaskForm):
    amount = IntegerField('Amount:')
    submit = SubmitField('Add to basket')

class CheckoutForm(FlaskForm):
    line1 = StringField('Address line 1:') 
    line2 = StringField('Address line 2:')
    line3 = StringField('Address line 3:')
    city = StringField('City:')
    country = StringField('Country:')
    postcode = StringField('Post Code:')
    submit = SubmitField('Submit')

class PaymentForm(FlaskForm):
    card_name = StringField('Card Name:')
    card_no = IntegerField('Card Number:')
    card_exp = StringField('Card Expiration Date:')
    cvv = IntegerField('cvv')
    submit = SubmitField('Finalise Puchase')
    
