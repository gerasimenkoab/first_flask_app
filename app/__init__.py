from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app) # creating database instance for app
migrate = Migrate(app,db) # creating db migration instance for app and db object

from app import routes

