# flask-simple-demo
flask-simple-demo

## Installation

```
$ [sudo] pip install virtualenv
$ virtualenv env
$ . env/bin/activate
(venv) $ pip install -r requirements.txt
```

## Start to development and running server

run server
```
$ . env/bin/activate
$ python run.py

# open this url in your browser
# http://127.0.0.1:5000/
```

### Demo Resource

 - /demo
 - /demoB/<user>
 - /cookie

## Learning points

### 增加 RESTful API Resource方式

``` python
# 1)
@api.resource('/api-path')
class Demo(Resource):
    return {'msg' : 'OK'}
# 2)
api.add_resource(Demo, '/api-path')

```
