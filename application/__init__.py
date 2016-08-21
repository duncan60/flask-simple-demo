# -*- coding: utf-8 -*-
import json
from flask import Flask, url_for, redirect, session
from flask import make_response, render_template

from flask.ext import restful
from flask.ext.restful import Resource

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config.default')
app.config.from_pyfile('config.py')
app.config.from_envvar('APP_CONFIG_FILE')

api = restful.Api(app)

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

@app.errorhandler(404)
def resource_not_found(error):
   return redirect(url_for('error-resource'))


from application.RESTful import demo
