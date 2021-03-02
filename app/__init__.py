from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

#initializing app
app = Flask(__name__)

#initializing Flask extensions
bootstrap = Bootstrap(app)

#setting up configuration
app.config.from_object(DevConfig)

from app import views
