# flask-simple-demo
flask-simple-demo


### 增加 RESTful API Resource方式

``` python
# 1)
@api.resource('/api-path')
class Demo(Resource):
    return {'msg' : 'OK'}
# 2)
api.add_resource(Demo, '/api-path')

```
