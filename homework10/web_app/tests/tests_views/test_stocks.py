from flask import url_for
import pytest
from app import app
# from web_app.models import db
from web_app.views import add_stock_to_db,create_stock
from web_app.models.stocks import Stock_db
import random
from web_app.models import db

@pytest.fixture
def client():
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client

@pytest.fixture
def data():
    print('haha===============================')
    db.session.query(Stock_db).delete()
    db.session.commit()
    test = Stock_db.query.filter_by(name='TEST').one_or_none()
    if test is not None:
        Stock_db.query.filter_by(name='TEST').delete()
    else:
        add_stock_to_db('TEST')
    yield 0
    Stock_db.query.filter_by(name='TEST').delete() # teardown
    db.session.commit()

def test_add_stock(client,data):
    assert Stock_db.query.filter_by(name='TEST').count() == 1

def test_stock_creation(client):
    initial_c = (Stock_db.query.count())
    list0 = ['one1','two2','spam','eggs']
    for names in list0:
        add_stock_to_db(names)
    count_all = (Stock_db.query.count())
    for names in list0:
        Stock_db.query.filter_by(name=names).delete()
        db.session.commit()
    db.session.commit()
    assert count_all == 4 + initial_c

def test_add_stock_post(client):
    test_stock = {'stock_ticker':'jdjd'}
    url = url_for('stocks_app.add')
    res = client.post(url,data=test_stock,
                      mimetype='application/x-www-form-urlencoded')
    assert res.status_code < 400

def test_add_stock_post_exists(client):
    def func():
        test_stock = {'stock_ticker':'jdjd'}
        url = url_for('stocks_app.add')
        res = client.post(url,data=test_stock,
                          mimetype='application/x-www-form-urlencoded')
        return res
    func()
    rez = func()
    assert rez.status_code
    assert rez.status_code == 500

def test_dull_test(client,data):
    url = url_for("stocks_app.test")
    response = client.delete(url)
    data = response.json
    print('data content is ', data)
    assert data == {'ok':True}

def test_add_stocks_get(client):
    url = url_for('stocks_app.add')
    response = client.get(url)
    data = response
    print('data content is ===== ', data)
    # assert str(response) == '<Response streamed [200 OK]>'
    assert response.status_code < 400


# def test_add_stocks_post(client):
#     st0 = create_stock('kaka')
#     print('st0 type is -------------- ',st0.name)
#     url = url_for('stocks_app.add')
#     response = client.post(url, data=st0,
#                       mimetype='application/x-www-form-urlencoded')
#     # assert str(response) == '<Response streamed [200 OK]>'
#     assert response.status_code < 400


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

# def test_dull_test(client):
#     url = url_for("stocks_app.test")
#     response = client.delete(url)
#     data = response.json
#     print('data content is ', data)
#     assert data == {'ok':True}


#add FUNCTION!!!!
# def add_stock_to_db(ticker: str):
#     test_stock = Stock_db()
#     test_stock.name = ticker
#     test_stock.price = random.randint(0, 99)
#     db.session.add(test_stock)
#     db.session.commit()
#     return 0



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

# def test_add_methods(client):
#     url = url_for("add")
#     response = client.get(url)
#     rez = 0
#     if '200 OK' in str(response):
#         rez = 1
#     else:
#         rez = 0
#     assert rez == 1

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
