from flask import g
from itsdangerous import TimedJSONWebSignatureSerializer as JWT

from application import app, auth

jwt = JWT(app.config['SECRET_KEY'], expires_in=3600)


users = [
    {
        'group': 'abc_group',
        'name': 'john'
    },
    {
        'group': 'def_group',
        'name': 'duncan'
    }
]

for user in users:
    token = jwt.dumps({'user': user})
    print('*** token for {}: Authorization:Bearer {}\n'.format(user, token))


@auth.verify_token
def verify_token(token):
    g.user = None
    try:
        data = jwt.loads(token)
    except:
        return False
    print('>>>>>>>>>>>%s' % data)
    if 'user' in data:
        g.user = data['user']
        return True
    return False


@app.route('/auth')
@auth.login_required
def authIndex():
    return "Hello, %s!" % g.user
