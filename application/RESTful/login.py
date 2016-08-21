from flask import abort, g,request, make_response
from flask.ext.restful import Resource, reqparse
from flask.ext.login import login_user, current_user, UserMixin, user_login_confirmed
from application import app, api, login_manager
from application.RESTful.error import InvalidUsage

class User(UserMixin):
    pass

@app.before_request
def before_request():
    g.user = current_user

@login_manager.user_loader
def user_loader(id):
    user = User()
    user.id = id
    return user

@login_manager.unauthorized_handler
def unauthorized():
    return {'msg': 'you need login required'}, 401

class Login(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type = str, help = u'No task name provided')
        self.reqparse.add_argument('password', type = str, help = u'No password price provided')

    def get(self):
        args = self.reqparse.parse_args()

        if not args['name'] or not args['password']:
            raise InvalidUsage('INVALID REQUEST', status_code=400)

        if g.user.is_authenticated:
            return {
                'msg'  : 'alerady login',
                'token': request.cookies.get(app.config['REMEMBER_COOKIE_NAME'])
            }, 201

        try:
            #check user account
            # find_user = mongo.db.user.find_one(
            #     {
            #         'name'    : args['name'],
            #         'password': args['password']
            #     }
            # )
            pass
        except:
            return {'msg': 'DB Error'}, 500

        if not find_user:
            msg = 'name or passowrd error'
            return {'msg': 'name or passowrd error'}, 201
        else:
            user = User()
            user.id = find_user['_id']
            login_user(user, remember=True)
            token = request.cookies.get(app.config['REMEMBER_COOKIE_NAME'])
            # update user
            # mongo.db.user.find_one_and_update(
            #     {'_id': user.id},
            #     {'$set': {
            #                 'date_latest_login': datetime.utcnow(),
            #                 'token'            : token
            #             }
            #     }
            # )
            return {
                'msg'  : 'login success',
                'token': token
            }, 201

api.add_resource(Login, '/login', endpoint = 'login')
