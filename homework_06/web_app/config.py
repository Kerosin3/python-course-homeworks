from os import getenv

SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI","postgresql://USER:PASSWORD@localhost:5432/STOCKS_DB")

class Config(object): #default
    DEBUG = True
    TESTING = False
    DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DATABASE_URI = SQLALCHEMY_DATABASE_URI
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
