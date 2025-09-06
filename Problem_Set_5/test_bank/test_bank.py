from bank import value

def test_value():
    assert value("") == 100
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("what's up") == 100
    assert value("Hello") == 0
    assert value("h") == 20
    assert value("Hi") == 20
    assert value(" hello") == 100