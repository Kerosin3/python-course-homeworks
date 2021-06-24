import config
from flask import Flask, render_template
from web_app.models.database import db
from flask_migrate import Migrate
from os import getenv
from web_app.views import stocks_app
import config

SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI", "postgresql://USER:PASSWORD@localhost:5432/STOCKS_DB")

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://USER:PASSWORD@database_local:5432/STOCKS_DB'
app.config.from_object("config.DevelopmentConfig")  # not working!!

app.register_blueprint(stocks_app)

db.init_app(app)
migrate = Migrate(app, db)  # откуда он знает про db?


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
    return render_template("test_page.html")


@app.cli.command(help="create all tables")
def create_all_tables():
    with app.app_context():
        migrate.upgrade()


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000") #REQUIRED!
