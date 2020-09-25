import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "fijsdofjweoirjfoeifjiofjoiwefjeofij"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost/flask_rest_live"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost/flask_rest_dev"


class TestingConfig(Config):
    DEVELOPMENT = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@nmkzh-testing-001.nomoko.lan/flask_rest_test"
