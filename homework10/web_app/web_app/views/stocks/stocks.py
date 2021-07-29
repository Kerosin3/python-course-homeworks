import random

from flask import request, Blueprint, jsonify, render_template, url_for, redirect
from werkzeug.exceptions import BadRequest, InternalServerError
from web_app.models.stocks import Stock_db
from web_app.models import db

stocks_app = Blueprint("stocks_app",
                       __name__,
                       url_prefix="/stocks"
                       )


def add_stock_to_db(ticker: str):
    test_stock = Stock_db()
    test_stock.name = ticker
    test_stock.price = random.randint(0, 99)
    db.session.add(test_stock)
    db.session.commit()
    return 0

def create_stock(ticker: str):
    test_stock = Stock_db()
    test_stock.name = ticker
    test_stock.price = random.randint(0, 99)
    # db.session.add(test_stock)
    # db.session.commit()
    return test_stock

@stocks_app.route("/<string:stock_ticker>/")
def get_stock(stock_ticker):
    stock0 = Stock_db.query.filter_by(name=stock_ticker).one_or_none()
    if (db.session.query(Stock_db).
            filter(Stock_db.name == stock_ticker).
            one_or_none()) is not None:  # stock_ticker not in STOCKS_DB:
        return render_template("stocks/details.html", stock=stock0)
    else:
        url = url_for("stocks_app.list")
        return redirect(url)


@stocks_app.route("/list/")
def list():
    stocks_all = Stock_db.query.all()
    return render_template("stocks/list.html", stocks=stocks_all)


@stocks_app.route("/")
def main_page():
    """
    just redirecting
    """
    url = url_for("stocks_app.list")
    return redirect(url)


@stocks_app.route("/add/", methods=["GET", "POST"],endpoint='add') #,endpoint='add'
def add_stock():
    if request.method == "GET":  # returning a template
        return render_template("stocks/add_stock.html")
    # if POST METHOD
    stock_ticker = request.form.get("stock_ticker")
    if not stock_ticker:
        db.session.rollback()
        raise BadRequest('stock ticker is required')
    if Stock_db.query.filter_by(name=stock_ticker). \
            one_or_none() is not None:
        db.session.rollback()
        raise InternalServerError('There is already such stock in DB')
    else:  # no stuch stock in db
        stock0 = Stock_db()
        stock0.name = stock_ticker
        stock0.price = random.randint(1, 99)
        # add_stock_to_db(stock=stock0)
        db.session.add(stock0)
        db.session.commit()
    url = url_for("stocks_app.list")
    return redirect(url)


@stocks_app.route("/plot/",endpoint='plot')
def plot():
    return "This feature has not been implemented yet, but we are working hard"


@stocks_app.route("/remove/", methods=["GET", "POST"])
def remove_stock():
    stocks_all = Stock_db.query.all()
    if request.method == "GET":  # returning a template
        return render_template("stocks/remove.html", stocks=stocks_all)
    # if POST METHOD
    stock_ticker = request.form.get("stock_ticker")
    if not stock_ticker:
        raise BadRequest('stock ticker is required')
    elif (obj := db.session.query(Stock_db).
            filter(Stock_db.name == stock_ticker).
            one_or_none()) is not None:  # stock_ticker not in STOCKS_DB:
        db.session.delete(obj)
        db.session.commit()
        url = url_for("stocks_app.list")
        return redirect(url)
    else:
        db.session.rollback()
        raise BadRequest('No such stock')

#not working
@stocks_app.route('/reset/',methods=['DELETE'],endpoint='reset')
def reset_stocks():
    # db.session.query(Stock_db).delete()
    # db.session.commit()

    # # print('all stocks',stocks_all)
    try:
        stocks = Stock_db.query.all()
        Stock_db.db.session.delete(stocks)
        # stocks_all = Stock_db.query.all()
    #     c=0
    #     for s in stocks_all:
    #         c+=1
    #         db.session.delete(s)
    #     print('C is == ',c)
        # db.session.query(Stock_db).delete()
        # # stockz.delete()
        # # print('stocks are ================ ',stockz)
        # stocks_all = Stock_db.query.all()
        # db.session.query(Stock_db).delete()
        # db.session.commit()
        return {'ok': True}
    except:
        db.session.rollback()
        return {'ok': False}


@stocks_app.route('/c&d/', methods=['DELETE'], endpoint='c&d')
def c_and_d():
    test_ticker = 'LLLL'
    add_stock_to_db(test_ticker)
    obj = db.session.query(Stock_db).filter(Stock_db.name == test_ticker).one_or_none()  # stock_ticker not in STOCKS_DB:
    if obj is not  None:
        db.session.delete(obj)
        db.session.commit()
        return {'ok': True}
    else:
        return {'ok': False}

@stocks_app.route('/test/', methods=['DELETE'], endpoint='test')
def dull_func():
    return {'ok': True}
