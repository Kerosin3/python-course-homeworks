from os import getenv

from flask import Flask, render_template
from flask_migrate import Migrate

from web_app.models.database import db
from web_app.views import stocks_app

import config

app = Flask(__name__)
# app.config.update(SERVER_NAME='localhost:5000')
# app.config.update(SERVER_NAME='myapp.dev:5000')
app.config['SERVER_NAME'] = '0.0.0.0:5000'
workmode = getenv("FLASK_ENV", 'development')

if workmode == 'development':
    config_app = config.DevelopmentConfig
elif workmode == 'production':
    config_app = config.ProductionConfig
elif workmode == 'test':
    config_app = config.TestingConfig
else:
    raise EnvironmentError('Not right mode of initialization, aborting')
app.config.from_object(config_app)
print('=========== current env:',config_app.ENV)
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
