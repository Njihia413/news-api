from re import DEBUG


class Config:
    '''
    Parent configuration class with general configuration settings
    '''
    pass

class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    '''
    DEBUG = True