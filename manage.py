from flask.ext.script import Manager

from application import app, socketio

manager = Manager(app)

if __name__ == '__main__':
    manager.run(socketio.run(app))
