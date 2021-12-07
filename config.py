import os
basedir = os.path.abspath(os.path.dirname(__file__))
STATIC_DIR = os.path.abspath('../static')
class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my secret key'
    UPLOAD_FOLDER = 'app/static/images'
    CSS_FOLDER ='app/static/styles'