import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = False
    # Flask-Restplus settings
    SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    ERROR_404_HELP = False


class DevelopmentConfig(Config):

    DEBUG = True
    # Flask settings
    SERVER_NAME = 'localhost:8081'
    FLASK_DEBUG = True

    # mongo db
    MONGO_DBNAME = 'hivery-db'
    MONGO_URI = "mongodb://localhost:27017/hivery-db"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    # Flask settings
    SERVER_NAME = 'localhost:8888'
    FLASK_DEBUG = True

    # mongo db
    MONGO_DBNAME = 'hivery-test-db'
    MONGO_URI = "mongodb://localhost:27017/hivery-test-db"





config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig
)

