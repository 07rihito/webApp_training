from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import Markup
from flask import request
from flask import abort
# from urllib.parse import urlparse
import mysql.connector

app = Flask(__name__)

@app.route("/")
def index():
  props = {'title': 'home'}
  return render_template('index.html', props=props)

@app.route("/about")
def about():
  props = {'title': 'About this app'}
  return render_template('about.html', props=props)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
