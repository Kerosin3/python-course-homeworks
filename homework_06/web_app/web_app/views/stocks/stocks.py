from flask import request, Blueprint, jsonify, render_template, url_for, redirect
from werkzeug.exceptions import BadRequest
from .stock_main import Stock,gen_stock_prices
# from models import Stock_db
from web_app.web_app.models.stocks import Stock_db

stocks_app = Blueprint("stocks_app",
                       __name__,
                       url_prefix="/stocks"
                       )
test_stock = Stock('Test',gen_stock_prices())
test_stock1 = Stock('Test_second',gen_stock_prices())
STOCKS_DB = {} #list[Stock]


def add_stock_to_db(stock:Stock):
    ticker = stock.ticker
    STOCKS_DB[ticker] = stock
    return 0


add_stock_to_db(stock=test_stock)
add_stock_to_db(stock=test_stock1)


@stocks_app.route("/<string:stock_ticker>/")
def get_stock(stock_ticker):
    return jsonify(stock_ticker=stock_ticker)


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


@stocks_app.route("/add/", methods=["GET","POST"])
def add_stock():
    if request.method == "GET": #returning a template
        return render_template("stocks/add_stock.html")
    #if POST METHOD
    stock_ticker = request.form.get("stock_ticker")
    if not stock_ticker:
        raise BadRequest('stock ticker is required')
    if stock_ticker in STOCKS_DB:
        raise BadRequest('Stock with this ticker is already added')
    else:
        stock0 = Stock(stock_ticker,gen_stock_prices())
        add_stock_to_db(stock=stock0)
    # STOCKS_DB.append(stock0)
    # url = url_for("stocks_app.get_stock",stock_ticker=stock0.ticker)
    url = url_for("stocks_app.list")
    return redirect(url)

@stocks_app.route("/plot/")
def plot():
    return "trying hard"


@stocks_app.route("/remove/", methods=["GET","POST"])
def remove_stock():
    if request.method == "GET": #returning a template
        return render_template("stocks/remove.html")
    #if POST METHOD
    stock_ticker = request.form.get("stock_ticker")
    if not stock_ticker:
        raise BadRequest('stock ticker is required')
    if stock_ticker not in STOCKS_DB:
        # MAKE POP UP NOT SUCH STOCK
        url = url_for("stocks_app.list")
        return redirect(url)
    else:
        del STOCKS_DB[stock_ticker]
        # url = url_for("stocks_app.get_stock",stock_ticker=stock0.ticker)
        url = url_for("stocks_app.list")
        return redirect(url)
