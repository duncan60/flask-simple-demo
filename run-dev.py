#!flask/bin/python
import os
basedir = os.path.abspath(os.path.dirname(__file__))

from application import app
app.run(debug = True, threaded=True)
#http://www.pythondoc.com/flask/api.html#flask.Flask.run
#app.run(host=None, port=None, debug=None, threaded=None, **options)
