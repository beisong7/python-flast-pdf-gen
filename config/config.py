# from os import environ, path
from dotenv import load_dotenv
import os

# basedir = path.abspath(path.dirname(__file__))
# load_dotenv(path.join(basedir, '.env'))

basedir = os.path.abspath(os.path.dirname(__file__))

# Navigate up to the root directory of your project
rootdir = os.path.abspath(os.path.join(basedir, '..'))

# Load the .env file from the root directory
load_dotenv(os.path.join(rootdir, '.env'))

class Config:
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
