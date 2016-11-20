# -*- coding: utf-8 -*-
import json
from flask import Flask, make_response, render_template

from flask.ext import restful
from flask.ext.login import LoginManager
from flask_socketio import SocketIO
from flask_httpauth import HTTPTokenAuth

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config.default')
app.config.from_pyfile('config.py')
app.config.from_envvar('APP_CONFIG_FILE')

login_manager = LoginManager()
login_manager.init_app(app)

socketio = SocketIO(app)

api = restful.Api(app)
auth = HTTPTokenAuth('Bearer')


@api.representation('application/json')
def output_json(obj, code, headers=None):
    resp = make_response(json.dumps(obj), code)
    resp.headers.extend(headers or {})
    return resp


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)



from application.resource import demo, error, login, logout, authg
from application.socket import simple
