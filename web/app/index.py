from flask import render_template
from flask import redirect
from flask import url_for
from flask import Markup
from flask import request
from flask import abort
# from urllib.parse import urlparse
import mysql.connector

from dbModels import Users
from application import app
from application import db

## Create Flask Application
#app = Flask(__name__)
## Set Config Class
#app.config.from_object('config.Config')
## Set DB
#db = SQLAlchemy(app)


@app.route('/')
def index():
  props = {'title': 'home'}
  return render_template('index.html', props=props)

@app.route('/about')
def about():
  props = {'title': 'About this app'}
  return render_template('about.html', props=props)

@app.route('/userList')
def userlist():
  try:
    users = Users.query.all()
    props = {'title': 'userList'}
    # TODO db接続テスト用に登録user一覧ページを作成する．将来的には管理者しか見れないように
    return render_template('userList.html', users=users, props=props)
  except Exception as e:
    props = {'title': 'error'}
    props['errorMsg'] = e
    return render_template('errorPage.html', props=props)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=False)
