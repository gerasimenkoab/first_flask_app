from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import RotatingFileHandler
import os
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app) # creating database instance for app
login = LoginManager(app)
login.login_view = 'login' # define login page for auto-redirect
from app import models
migrate = Migrate(app, db) # creating db migration instance for app and db object

from app import routes,errors

# adding api blueprint 
from app.api import bp as app_bp
app.register_blueprint( app_bp, url_prefix = '/api' )


if not app.debug:
    # if not in the debug mode
    if not os.path.exists('logs'):
        os.mkdir('logs')
    # creating logfile handler. Type - rotatingFileHandler
    file_handler = RotatingFileHandler( 'logs/microblog.log', maxBytes = 1024, backupCount = 10 )
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathmname)s: %(lineno)d]'
    ))
    file_handler.setLevel( logging.INFO )
    app.logger.addHandler( file_handler )
    app.logger.setLevel( logging.INFO )
    #app.logger.info('Microblog startup')