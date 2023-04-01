from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app) # creating database instance for app
login = LoginManager(app)
login.login_view = 'login' # define login page for auto-redirect
from app import models
migrate = Migrate(app, db) # creating db migration instance for app and db object

from app import routes

