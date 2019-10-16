from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import app_config


SERVER_MODE = 'development'


app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config[SERVER_MODE])

db = SQLAlchemy(app)
db.app = app
db.init_app(app)


import radio.views
