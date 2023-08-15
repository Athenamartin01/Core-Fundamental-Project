from application import app, db
from application.models import *
from flask import render_template,request,redirect,url_for
from flask_bcrypt import generate_password_hash

@app.route('/')
@app.route('/Home')
def home():
    basket = Order.query.filter_by(is_complete = False).first()
    if not(basket):
        new_cust = Customer()
        basket = Order(customerbr=new_cust)
        db.session.add(new_cust)
        db.session.add(basket)
        db.session.commit()
    return render_template('home.html')

@app.route('/Product Listings')
def product_listing():
    prod = Product.query.all()
    prod_tup=list((i,str(i.id)) for i in prod)
    return render_template('prod_list.html',products=prod_tup)

@app.route('/Categories', methods=['GET','POST'])
def categories():
    form = CategoryForm()
    unique_cat = set()
    category=""
    for i in Product.query.all():
        unique_cat.add(i.category)

    if request.form:
        category = request.form.get('category')

    prod = Product.query.filter_by(category=category).all()
    prod_tup=list((i,str(i.id)) for i in prod)
    return render_template('categories.html',products=prod_tup,form=form,unique_cat=unique_cat)
    
@app.route('/Cart', methods = ['GET','POST'])
def cart():
    basket = Order.query.filter_by(is_complete=False).first()
    order_prod = Order_Product.query.filter_by(orderbr=basket).all()

    prod = []
    for i in order_prod:
        if i.amount == 0:
            order_prod.remove(i)
            continue
        prod.append(Product.query.filter_by(id=i.prod_id).first())
    prod = zip(prod,order_prod)

    prod_tup=list((i[0],str(i[0].id),i[1]) for i in prod)
    total = 0
    for product in prod_tup:
        total += product[0].price * product[2].amount

    form_list = []
    for i in prod_tup:
        form_list.append(Item_to_Basket_Form())

    if any(request.form for form in form_list):
        for i,form in enumerate(form_list):
            amount =  request.form.get(str(prod_tup[i][0].id))
            if amount == None:
                continue
            prod_tup[i][2].amount = int(amount) 
            db.session.commit()
        return redirect(url_for('cart'))


    return render_template('cart.html',order=basket,prod=prod_tup,total=round(total,2),form_list=form_list)
    
@app.route('/Checkout', methods = ['GET','POST'])
def checkout():
    form = CheckoutForm()
    if request.form:
        basket = Order.query.filter_by(is_complete=False).first()
        customer = Customer.query.filter_by(id = basket.cust_id).first()
        line1 = request.form.get('line1')
        line2 = request.form.get('line2')
        line3 = request.form.get('line3')
        city = request.form.get('city')
        pc = request.form.get('pc')
        customer.add_line1 = line1
        customer.add_line2 = line2
        customer.add_line3 = line3
        customer.city = city
        customer.postcode = pc
        db.session.commit()
        return redirect(url_for('payment'))
    return render_template('checkout.html', form=form)



@app.route('/Payment',methods = ['GET','POST'])
def payment():
    form = PaymentForm()
    if request.form:
        basket = Order.query.filter_by(is_complete=False).first()
        customer = Customer.query.filter_by(id = basket.cust_id).first()
        card_name = request.form.get('card_name')
        card_no = generate_password_hash(request.form.get("card_no"))
        card_exp = f'{request.form.get("exp1")}/{request.form.get("exp2")}'
        cvv = generate_password_hash(request.form.get("cvv"))
        customer.card_name = card_name
        customer.card_no = card_no
        customer.card_exp = card_exp
        customer.cvv = cvv
        db.session.commit()
        return redirect(url_for('pay_success'))
    return render_template('payment.html', form=form)
    
@app.route('/Contact')
def contacts():
    return render_template('contacts.html')
    
@app.route('/About Us')
def about_us():
    return render_template('about_us.html')

@app.route('/<int:id>', methods=['GET','POST'])
def single_product(id:int):
    form = Item_to_Basket_Form()
    prod = Product.query.filter_by(id=id).first()
    prod_prodid= [prod,str(prod.id)]
    basket = Order.query.filter_by(is_complete=False).first()
    
    print(Order_Product.query.filter_by(productbr=prod,orderbr=basket).count())
    if Order_Product.query.filter_by(productbr=prod,orderbr=basket).count() == 0:
        order_prod = Order_Product(productbr=prod,orderbr=basket,amount=0)
        db.session.add(order_prod)
        db.session.commit()             
    else:
        order_prod = Order_Product.query.filter_by(productbr=prod,orderbr=basket).first()

    if request.form:
        amount = request.form.get('amount')
        order_prod.amount = int(order_prod.amount) + int(amount) 
        db.session.commit()
    return render_template('single_product.html',product=prod_prodid, form=form,pending=(prod.stock-order_prod.amount))

@app.route('/Payment Success')
def pay_success():
    basket = Order.query.filter_by(is_complete=False).first()
    basket.is_complete = True
    db.session.commit()

    order_prod = Order_Product.query.filter_by(orderbr=basket).all()
    for i in order_prod:
        prod = Product.query.filter_by(id=i.prod_id).first()
        prod.stock = prod.stock - i.amount
        db.session.commit()


    return render_template('pay_success.html')