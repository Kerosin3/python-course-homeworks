from flask import Flask, render_template,jsonify,Blueprint
from stocks.stocks import stocks_app

app = Flask(__name__)

app.register_blueprint(stocks_app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/products/")
def products():
    return render_template("products.html")


@app.route("/products/add/")
def add():
    return render_template("add.html")


@app.route("/test/")
def test():
    # return jsonify(stock1)
    return render_template("test_page.html")
