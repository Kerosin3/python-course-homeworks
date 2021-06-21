import config
from flask import Flask, render_template

import web_app.web_app.config.config
from .web_app.views.stocks.stocks import stocks_app
# from web_app.web_app.models import db
# from .web_app.models import db
from web_app.web_app.models.database import db
from flask_migrate import Migrate
from os import getenv

SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI", "postgresql://USER:PASSWORD@localhost:5432/STOCKS_DB")



app = Flask(__name__)

# app.config.from_object('config.DevelopmentConfig')


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://USER:PASSWORD@localhost:5432/STOCKS_DB'


# current_config = web_app.web_app.config.config.ProductionConfig
# current_config = web_app.web_app.config.config.TestingConfig
current_config = web_app.web_app.config.config
# print("===========")
# print(current_config.DevelopmentConfig.DATABASE_URI)
# print("===========")
# print('debug is ',current_config.DevelopmentConfig.DEBUG)
# print("===========")
# print('env=',current_config.DevelopmentConfig.ENV)
# # app.config.from_object('current_config.DevelopmentConfig')
# print("===========")
# print('env=',current_config.DevelopmentConfig)
from web_app.web_app.config.config import DevelopmentConfig
# app.config.from_object(DevelopmentConfig)
# print("env is",app.config['ENV'])
# app.config['FLASK_ENV'] = 'development'
# app.config['ENV'] = 'development'
# app.config.update()
# print("env is",app.config['ENV'])

# app.config['DEBUG'] = True

# app.config.from_object(config.config.)

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

# if __name__ == '__main__':
#     app.run()
