import os
from dotenv import load_dotenv


class BaseConfig(object):
    """Base configuration class"""
    load_dotenv()

    SECRET_KEY = os.getenv('DEV_SECRET_KEY')
    DEBUG = os.getenv("DEBUG")
    TESTING = False

class ProductionConfig(BaseConfig):
    """Production configuration class"""
    DEBUG=False
    SECRET_KEY=os.getenv('PROD_SECRET_KEY')

class DevConfig(BaseConfig):
    DEBUG=True
    TESTING=True