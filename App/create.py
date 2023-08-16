from application import app,db
from application.models import Product,Customer,Order


with app.app_context():
    db.drop_all()
    db.create_all() #inserts all data into database

    
    poker_table_green = Product(name='Poker Table (Green)',category='Tables',price=39.99,stock=10,desc='This is a 6 person poker table with Blacker leather rim and green felt.',image='1.png')
    poker_table_red = Product(name='Poker Table (Red)',category='Tables',price=49.99,stock=10,desc='This is an 9 player poker table with black leather rim and red felt.',image='2.png')

    playing_card_red = Product(name='Playing Cards (Red)',category='Cards',price=6.99,stock=5,desc='This is a red pack of plastic Bicycle playing cards.',image='3.png')
    playing_card_blue = Product(name='Playing Cards (Blue)',category='Cards',price=6.99,stock=0,desc='This is a blue pack of plastic Bicycle playing cards.',image='4.png')

    db.session.add(poker_table_green)
    db.session.add(poker_table_red)
    db.session.add(playing_card_blue)
    db.session.add(playing_card_red)


    db.session.commit()