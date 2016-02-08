# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, request
from flask.ext.triangle import Triangle
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
Triangle(app)

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
    return jsonify(data);

app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
