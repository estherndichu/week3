import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://moringa:Access@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}