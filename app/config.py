import os

class Config(object):
    APPNAME = 'app'
    ROOT = os.path.abspath(APPNAME)
    UPLOAD_PATH = '/static/upload/'
    SERVER_PATH = ROOT + UPLOAD_PATH
    SERVER_PATH_DOCS = SERVER_PATH + 'docs'

# Database configuration
    USER = os.environ.get('POSTGRES_USER', '') # Set your default username here
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', '1234')
    HOST = os.environ.get('POSTGRES_HOST', 'postgres')
    PORT = os.environ.get('POSTGRES_PORT', '5432')
    DB = os.environ.get('POSTGRES_DB', 'mydb')

    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    SECRET_KEY = 'fe32t5t5t4'
    SQLALCHEMY_TRACK_MODIFICATIONS = True