import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    DATABASE_ENGINE = os.environ.get('DATABASE_ENGINE', 'postgresql')
    DATABASE_HOST = os.environ.get('DATABASE_HOST', 'localhost')
    DATABASE_PORT = os.environ.get('DATABASE_PORT', '5432')
    DATABASE_NAME = os.environ['DATABASE_NAME']
    DATABASE_USER = os.environ['DATABASE_USER']
    DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', '')
    SQLALCHEMY_DATABASE_URI = (f'{DATABASE_ENGINE}://{DATABASE_USER}:{DATABASE_PASSWORD}@'
                               f'{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
