#from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import dbConfig
import dbHandler
# Create Flask Application
app = Flask(__name__)


# sqlAlchemy用------------------------------------------------
## Set Config Class
#app.config.from_object('dbConfig.Config')
#
## applocation.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
## Set DB
#db = SQLAlchemy(app)
#-------------------------------------------------------------

# PyMySQL用------------------------------------------------
host = 'my-db-host'
port = 3306
user = 'root'
password = 'RootPass'
db_name = 'app'
cursor_mode = "aaa"
db = dbHandler.DBHandler(host,port,user,password,db_name)

if __name__ == "__main__":
  host = 'my-db-host'
  port = 3306
  user = 'root'
  password = 'RootPass'
  db_name = 'app'
  cursor_mode = "aaa"
  db = dbHandler.DBHandler(host,port,user,password,db_name)
  print(db.executeQuery())
