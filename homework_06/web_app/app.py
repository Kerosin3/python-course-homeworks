from os import getenv

from flask import Flask, render_template
from flask_migrate import Migrate

from web_app.views import stocks_app
from web_app.models.database import db


app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

app.register_blueprint(stocks_app)

db.init_app(app)
migrate = Migrate(app,db) #откуда он знает про db?


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


@app.cli.command(help="create all tables")
def create_all_tables():
    with app.app_context():
        migrate.upgrade()


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")
