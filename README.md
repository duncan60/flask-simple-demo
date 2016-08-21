# flask-simple-demo
flask-simple-demo

## Installation

```
$ [sudo] pip install virtualenv
$ virtualenv env
$ . env/bin/activate
(venv) $ pip install -r requirements.txt

# or if use pyenv virtualenv

$ pyenv virtualenv [python version] [virtualenv name]
$ pyenv local [virtualenv name]
(virtualenv name) $ pip install -r requirements.txt
```

## Start to development and running server

run server
```
$ . env/bin/activate
# if had setting pyenv local, can pass '. env/bin/activate' command
$ python run.py

# open this url in your browser
# http://127.0.0.1:5000/
```

### API Resource

 - /demo
 - /demoB/[username]
 - /cookie

## Learning points

### 使用 pyenv 建立不同版本開發環境

 - [用pyenv和virtualenv搭建python虚拟环境](http://www.tiny-coder.com/home-article-51.html)
 - install failed 的處理：[pyenv/issues/454](https://github.com/yyuu/pyenv/issues/454)
 - [command Reference](https://github.com/yyuu/pyenv/blob/master/COMMANDS.md)

### config 配置

 - [變量配置](https://spacewander.github.io/explore-flask-zh/5-configuration.html)
 - [Flask生成SECRET_KEY（密钥）的一种简单方法](http://flask123.sinaapp.com/article/41/)

### session
 - [flask session](http://www.pythondoc.com/flask/quickstart.html#sessions)
 - [Using sessions in Flask](http://code.runnable.com/Uhf58hcCo9RSAACs/using-sessions-in-flask-for-python)

### coolkie
 - [flask cookies](http://www.pythondoc.com/flask/quickstart.html#cookies)

### 增加 RESTful API Resource方式

``` python
# 1)
@api.resource('/api-path')
class Demo(Resource):
    return {'msg' : 'OK'}
# 2)
api.add_resource(Demo, '/api-path')

```
