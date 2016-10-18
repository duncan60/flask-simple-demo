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
# cd to project folder path
$ pyenv local [virtualenv name]
(virtualenv name) $ pip install -r requirements.txt

# create instance/config.py, set value
SESSION_COOKIE_NAME = 'yourapplication'
REMEMBER_COOKIE_NAME = 'yourapplication'
SECRET_KEY = 'yoursecretkey'
```

## Start to development and running server

```
$ . env/bin/activate
# if had setting pyenv local, can pass '. env/bin/activate' command
$ python run.py

# open this url in your browser
# http://127.0.0.1:5000/
```
## Run testing

```
$ python test.py --cov-report=term  --cov=application/ test/
# or output testing report
$ python test.py --cov-report=term --cov-report=html --cov=application/ test/
```

### API Resource

 - /demo
 - /demoB/[username]
 - /cookie
 - /login
 - /logout

## Learning points

### 使用 pyenv 建立不同版本開發環境

 - [用pyenv和virtualenv搭建python虚拟环境](https://zhuanlan.zhihu.com/p/22147581)
 - [使用 Pyenv 管理多個 Python 版本](http://blog.codylab.com/python-pyenv-management/)
 - install failed 的處理：[pyenv/issues/454](https://github.com/yyuu/pyenv/issues/454)
 - [command Reference](https://github.com/yyuu/pyenv/blob/master/COMMANDS.md)

### config 配置

 - [變量配置](https://spacewander.github.io/explore-flask-zh/5-configuration.html)
 - [Flask生成SECRET_KEY（密钥）的一种简单方法](http://flask123.sinaapp.com/article/41/)
 - [Flask-Script参考手册](https://github.com/nummy/flask-script-cn)

### output requirements.txt
 ```
 $ pip freeze > requirements.txt
 ```

### session

 - [flask session](http://www.pythondoc.com/flask/quickstart.html#sessions)
 - [Using sessions in Flask](http://code.runnable.com/Uhf58hcCo9RSAACs/using-sessions-in-flask-for-python)

### coolkie

 - [flask cookies](http://www.pythondoc.com/flask/quickstart.html#cookies)

### error handler

 - [Implementing API Exceptions](http://flask.pocoo.org/docs/0.11/patterns/apierrors/)

### login and logout

 - [flask-login](http://www.pythondoc.com/flask-login/index.html)
 - [如何使用 Flask-Login](http://jaychung.tw/2015/02/23/how-to-apply-flask-login/)

### unittest

 - [pytest](http://doc.pytest.org/en/latest/contents.html)
 - [Python单元测试框架之pytest -- fixtures](http://www.cnblogs.com/fnng/p/4769020.html)
 - [沒學會 fixtures 不要說會用 pytest – Part II](http://www.techurtime.com/pytest_fixtures_part2/)
 - [pytest fixture](http://senarukana.github.io/2015/05/29/pytest-fixture/)

### 增加 RESTful API Resource方式

``` python
# 1)
@api.resource('/api-path')
class Demo(Resource):
    return {'msg' : 'OK'}
# 2)
api.add_resource(Demo, '/api-path')

```
### linter for flaske8
- [Install and Configure the Atom Editor for Python](http://www.marinamele.com/install-and-configure-atom-editor-for-python)

設定：Preference > Package > Setting lint-flake8 > Ignore Error Code: E999
