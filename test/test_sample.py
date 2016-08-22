import pytest

def func(x):
    return x+1

def test_func2():
    assert func(4) == 5

#@pytest.fixture()

@pytest.fixture()
def hello():
    return "hello"

def test_string(hello):
    assert hello == "hello", "fixture should return hello"


#@pytest.mark.usefixtures

@pytest.fixture()
def prepare_data1():
    print('\nprepare_data1')

@pytest.fixture()
def prepare_data2():
    print('prepare_data2')

@pytest.mark.usefixtures('prepare_data1', 'prepare_data2')
def test_1():
    print('test_1()')

@pytest.mark.usefixtures('prepare_data1', 'prepare_data2')
def test_2():
    print('test_2()')


@pytest.mark.usefixtures('prepare_data1', 'prepare_data2')
class Test:
    def test_1(self):
        print('test_1() in class')

    def test_2(self):
        print('test_2() in class')

#pytest.fixture()
@pytest.fixture()
def some_data():
    data = {'foo':1, 'bar':2, 'baz':3}
    return data

def test_foo(some_data):
    assert some_data['foo'] == 1

#pytest.fixture(params)
@pytest.fixture(params=[1,2,3])
def test_data(request):
    return request.param

def test_not_2(test_data):
    print('test_data: %s' % test_data)
    assert test_data != 2
