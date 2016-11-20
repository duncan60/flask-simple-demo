# -*- coding: utf-8 -*-
import time
from flask.ext.restful import Resource
from flask import request, make_response, session, g

from application import app, api, auth

def sumSessionCounter():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1
    print ('counter: {0}'.format(session['counter']))


@app.route('/demo')
@auth.login_required
def Demo():
    sumSessionCounter()
    return "this is user name:, %s!" % g.user['name']


class DemoB(Resource):
    def get(self, user):
        resp = make_response('add cookies')
        resp.set_cookie(key='username', value=user, expires=time.time()+6*60)
        return resp


class GetCookie(Resource):
    def get(self):
        return {
            'message' : 'succeed',
            'code': '0',
            'result': {
                'cookie_username': request.cookies.get('username')
            }
        }, 200



#變量規則： http://www.pythondoc.com/flask/quickstart.html#id5
api.add_resource(DemoB, '/demoB/<user>', endpoint='demo-b')
api.add_resource(GetCookie, '/cookie', endpoint='cookie')
