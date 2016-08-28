# -*- coding: utf-8 -*-
from flask import request
from application import app, api, socketio
from flask_socketio import emit, disconnect

thread = None

def background_thread():
    count = 0
    while True:
        socketio.sleep(2)
        count += 1
        socketio.emit('serverResponse',
                      {'data': 'Server count:{0}'.format(count)},
                      namespace='/test')

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
    global thread
    if thread is None:
        thread = socketio.start_background_task(target=background_thread)
    emit('serverResponse', {'data': 'Connected'})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected:', request.sid)
