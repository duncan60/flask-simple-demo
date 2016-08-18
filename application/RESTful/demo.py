# -*- coding: utf-8 -*-
from __future__ import division
import time
from flask.ext.restful import Resource
from flask import request, make_response

from application import app, api

@api.resource('/demo', endpoint='demo-a')
class Demo(Resource):
    def get(self):
        return {
            'msg': 'succeed',
            'code': '0',
            'result': 'demo source'
        }, 200

class DemoB(Resource):
    # cookies: http://www.pythondoc.com/flask/quickstart.html#cookies
    def get(self, user):
        resp = make_response('add cookies')
        resp.set_cookie(key='username', value=user, expires=time.time()+6*60)
        return resp

class GetCookie(Resource):
    def get(self):
        return {
            'msg' : 'succeed',
            'code': '0',
            'result': {
                'cookie_username': request.cookies.get('username')
            }
        }, 200

class Error(Resource):
    def get(self):
        return {
          'msg': 'error'
        }, 404
#變量規則： http://www.pythondoc.com/flask/quickstart.html#id5
api.add_resource(DemoB, '/demoB/<user>', endpoint='demo-b')
api.add_resource(GetCookie, '/cookie', endpoint='cookie')
api.add_resource(Error, '/error', endpoint='error-resource')
