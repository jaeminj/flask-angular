# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, jsonify, request
from flask.ext.triangle import Triangle
from flask.ext.sqlalchemy import SQLAlchemy
from session import SqliteSessionInterface
from werkzeug.contrib.fixers import ProxyFix
from flask.ext.login import LoginManager

CONFIG_FILE = 'global.cfg'


app = Flask(__name__)

CONFIG_PATH = os.path.join(app.root_path, CONFIG_FILE)
app.config.from_object(CONFIG_FILE)
app.config.from_pyfile(CONFIG_PATH, silent=True)
util.save_config(app.config, CONFIG_PATH)

path = app.config['SESSION_PATH']                   
path = os.path.join(app.root_path, '.sessions')
if not os.path.exists(path):
    os.mkdir(path)
    os.chmod(path, int('700', 8))
app.session_interface = SqliteSessionInterface(path)

Triangle(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id',db.Integer , primary_key=True)
    username = db.Column('username', db.String(20), unique=True , index=True)
    password = db.Column('password' , db.String(10))
    email = db.Column('email',db.String(50),unique=True , index=True)
    registered_on = db.Column('registered_on' , db.DateTime)
    
    def __init__(self , username ,password , email):
        self.username = username
        self.password = password
        self.email = email
        self.registered_on = datetime.utcnow()


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index2.html')
def index2():
    return render_template('index2.html')


@app.route('/index3.html')
def index3():
    return render_template('index3.html')

@app.route('/api/hello')
def hello():
    resp = {
        'msg': 'hello'
    }
    return jsonify(resp)


@app.route('/api/goodbye', methods=['POST'])
def goodbye():
    msg = request.get_json(force=True)['msg']
    resp = {
        'msg': 'Goodbye ' + msg
    }
    return jsonify(resp)

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json(force=True);
    print(data)
    print(data['user_key'])
    print(data['user_id'])
    return jsonify(data)

app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
