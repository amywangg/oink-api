import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'secret'
    APP_SETTINGS = "config.DevelopmentConfig"
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DATABASE_URL = "postgresql://localhost/oink_db"
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
