# -*- coding: utf-8 -*-
from flask import request
from application import app, api, socketio
from flask_socketio import emit, disconnect

@socketio.on('clientEvent', namespace='/test')
def test_message(message):
    emit('serverResponse',
         {'data': 'server msg: {0} !!!'.format(message['data'])})

@socketio.on('disconnectRequest', namespace='/test')
def disconnect_request():
    emit('serverResponse',
         {'data': 'Disconnected!'})
    disconnect()

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('serverResponse', {'data': 'Connected'})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected:', request.sid)
