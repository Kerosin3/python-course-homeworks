from flask import url_for
import pytest
from app import app
# from web_app.models import db
from web_app.views import add_stock_to_db
from web_app.models.stocks import Stock_db
import random
from web_app.models import db

@pytest.fixture
def client():
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client

# @pytest.fixture(scope='session')
# def db(app):
#
#     db.app = app
#     db.create_all()
#
#     return db
# @pytest.fixture(scope='function')
# def session(session, db):
#     connection = db.engine.connect()
#     transaction = connection.begin()
#
#     #options = dict(bind=connection, binds={})
#     options = dict(bind=connection)
#     session = db.create_scoped_session(options=options)
#     yield session

def test_dull_test(client):
    url = url_for("stocks_app.test")
    response = client.delete(url)
    data = response.json
    print('data content is ', data)
    assert data == {'ok':True}


#add FUNCTION!!!!
# def add_stock_to_db(ticker: str):
#     test_stock = Stock_db()
#     test_stock.name = ticker
#     test_stock.price = random.randint(0, 99)
#     db.session.add(test_stock)
#     db.session.commit()
#     return 0

def test_add_stock(client):
     add_stock_to_db('TEST')

# #not working
# def test_add_stock(session):
#     # connection = db.engine.connect()
#     # transaction = connection.begin()
#     # options = dict(bind=connection)
#     # session = db.create_scoped_session(options=options)
#
#     test_stock = Stock_db()
#     test_stock.name = 'adas'
#     test_stock.price = random.randint(0, 99)
#     db.session.add(test_stock)
#     db.session.commit()
#     # transaction.rollback()
#     # connection.close()
#     # session.remove()

def test_add_methods(client):
    url = url_for("add")
    response = client.get(url)
    rez = 0
    if '200 OK' in str(response):
        rez = 1
    else:
        rez = 0
    assert rez == 1

# def test_reset_stocks(client):
#     url = url_for("stocks_app.reset")
#     # print('url is',url)
#     # print('TYPE OF THIS', type(url))
#     response = client.delete(url)
#     data = response.json
#     print('data content is ', data)
#     assert data == {'ok':True}
#
#
# def test_c_and_d(client):
#     url = url_for("stocks_app.c&d")
#     response = client.delete(url)
#     data = response.json
#     print('data content is ', data)
#     assert data == {'ok': True}
