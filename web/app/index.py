from flask import render_template
from flask import redirect
from flask import url_for
from flask import Markup
from flask import request
from flask import abort
# from urllib.parse import urlparse
import mysql.connector

#from dbModels import Users
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
    #users = Users.query.all()
    users = db.executeQuery()
    props = {'title': 'userList'}
    # TODO db接続テスト用に登録user一覧ページを作成する．将来的には管理者しか見れないように
    return render_template('userList.html', users=users, props=props)
  except Exception as e:
    props = {'title': 'error'}
    props['errorMsg'] = e
    return render_template('errorPage.html', props=props)


# add user operation
@app.route('/addUser', methods=['POST'])
def addUser():
  newUser = request.form['user']
  newMail = request.form['mail']
  newPass = request.form['pass']
  #new_user = Users(username=newUser, email=newMail, passwd=newPass)
  try:
    #db.session.add(new_user)
    #db.session.commit()
    db.insert(newUser, newMail, newPass)
    return redirect(url_for('userlist')) # defで定義されている関数へリダイレクトする
  except Exception as e:
    props = {'title': 'error'}
    props['errorMsg'] = e
    return render_template('errorPage.html', props=props)


## delete user operation
#@app.route('/delUser/<int:id>')
#def delUser(id):
#  deleteUser = Users.query.filter_by(id=id).first()
#  try:
#    db.session.delete(deleteUser)
#    db.session.commit()
#    return redirect(url_for('userlist'))
#  except Exception as e:
#    props = {'title': 'error'}
#    props['errorMsg'] = e
#    return render_template('errorPage.html', props=props)


# error page
@app.route('/errorPage')
def errorPage(e):
    props = {'title': 'error'}
    props['errorMsg'] = e
    return render_template('errorPage.html', props=props)


@app.errorhandler(404)
def page_not_found(error):
  return "error occurred: " + error


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=False)
