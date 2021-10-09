#from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import dbConfig
# Create Flask Application
app = Flask(__name__)

# Set Config Class
app.config.from_object('dbConfig.Config')

# applocation.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Set DB
db = SQLAlchemy(app)