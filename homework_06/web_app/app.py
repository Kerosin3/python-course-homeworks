from flask import Flask, render_template
from web_app.web_app.views.stocks.stocks import stocks_app
from web_app.web_app.models import db

from flask_migrate import Migrate

app = Flask(__name__)

# app.config.from_object('config.DevelopmentConfig')
app.register_blueprint(stocks_app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgesql://USER:PASSWORD@localhost:5432:/app'


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
