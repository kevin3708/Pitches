import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://kevin:Password2@localhost/pitches'
    

    @staticmethod
    def init_app(app):
        pass
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production': ProdConfig
}