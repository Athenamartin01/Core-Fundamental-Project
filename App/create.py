from application import app,db
from application.models import Product


with app.app_context():
    db.drop_all()
    db.create_all() #inserts all data into database

    
    poker_table_green = Product(name='Poker Table (Green)',category='Tables',price=99.99,stock=10,desc='This is a 6 person poker table with Blacker leather rim and green felt.',image='1.jpg')
    poker_table_red = Product(name='Poker Table (Red)',category='Tables',price=99.99,stock=10,desc='This is an 9 player poker table with black leather rim and red felt.',image='2.jpg')

    playing_card_red = Product(name='Playing Cards (Red)',category='Cards',price=6.99,stock=5,desc='This is a red pack of plastic Bicycle playing cards.',image='3.jpg')
    playing_card_blue = Product(name='Playing Cards (Blue)',category='Cards',price=6.99,stock=0,desc='This is a blue pack of plastic Bicycle playing cards.',image='4.jpg')

    poker_chip_set = Product(name='Poker Chip Set',category='Chips',price=29.99,stock=24,desc='This is a poker chip set including enough chips for 9 players, dealer button and 2 card packs.',image='5.jpg')
    poker_chips_1 = Product(name='Poker Chips (Cash, 1200pcs)', category='Chips',price=19.99,stock=4,desc='Poker chips for a cash game, 200 of each chip included.',image='6.jpg')
    poker_chips_2 = Product(name='Poker Chips (Tournament, 1200pcs)', category='Chips',price=19.99,stock=4,desc='Poker chips for a tournament game, 600 of each chip included.',image='7.jpg')

    db.session.add(poker_table_green)
    db.session.add(poker_table_red)
    db.session.add(playing_card_blue)
    db.session.add(playing_card_red)
    db.session.add(poker_chip_set)
    db.session.add(poker_chips_1)
    db.session.add(poker_chips_2)

    db.session.commit()