import os
from dotenv import load_dotenv


class BaseConfig(object):
    """Base configuration class"""
    load_dotenv()

    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = os.getenv("DEBUG")
    TESTING = os.getenv("TESTING")
    DB_NAME = os.getenv("DB_NAME")

class ProductionConfig(BaseConfig):
    """Production configuration class"""
    DEBUG=False
    SECRET_KEY=os.getenv('PROD_SECRET_KEY')
    DB_NAME = "tt_prod.db"

class DevConfig(BaseConfig):
    DEBUG=True
    TESTING=True
    DB_NAME="tt_dev.db"
    UPLOADS_FOLDER="static/uploads"