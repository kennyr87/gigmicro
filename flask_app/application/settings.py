 # Flask configuration object
 # @see http://flask.pocoo.org/docs/1.0/config/#configuration-basics
class Config(object):
    SECRET_KEY = 'REPLACE ME'

class ProdConfig(Config):
    ENV = 'prod'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'
    # CACHE_TYPE = 'simple'

class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True

    # SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'

    # CACHE_TYPE = 'null'

class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    TESTING = True

    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_file.name
    # SQLALCHEMY_ECHO = True
