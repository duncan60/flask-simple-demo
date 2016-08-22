def func(x):
    return x+1

def test_func():
    assert func(3) == 5

def test_func2():
    assert func(4) == 5

def test_answer(cmdopt):
    if cmdopt == "type1":
        print ("first")
    elif cmdopt == "type2":
        print ("second")
    assert 0 # to see what was printed
