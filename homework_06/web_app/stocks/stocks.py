from flask import request, Blueprint, jsonify, render_template, url_for, redirect
from werkzeug.exceptions import BadRequest
from .stock_main import Stock,gen_stock_prices


stocks_app = Blueprint("stocks_app",
                       __name__,
                       url_prefix="/stocks"
                       )
test_stock = Stock('Test',gen_stock_prices())
STOCKS_DB = [test_stock] #list[Stock]


@stocks_app.route("/<string:stock_ticker>/")
def get_stock(stock_ticker):
    return jsonify(stock_ticker=stock_ticker)


@stocks_app.route("/list/")
def list():
    return render_template("stocks/list.html",stocks=STOCKS_DB)


@stocks_app.route("/add/", methods=["GET","POST"])
def add_stock():
    if request.method == "GET": #returning a template
        return render_template("stocks/add_stock.html")
    #if POST METHOD
    stock_ticker = request.form.get("stock_ticker")
    if not stock_ticker:
        raise BadRequest('stock ticker is required')
    stock0 = Stock(stock_ticker,gen_stock_prices())
    STOCKS_DB.append(stock0)
    # url = url_for("stocks_app.get_stock",stock_ticker=stock0.ticker)
    url = url_for("stocks_app.list")
    return redirect(url)
