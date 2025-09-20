import pytest
from jar import Jar


def test_init():
    with pytest.raises(ValueError):
       jar = Jar(-1, 0)


def test_str():
    jar = Jar(12,0)
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(8)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(12,0)
    assert jar.deposit(1) == None
    assert jar.deposit(10) == None
    assert jar.deposit(2) == ValueError
    assert jar.deposit(-1) == ValueError


def test_withdraw():
    jar = Jar(12,10)
    assert jar.withdraw(1) == None
    assert jar.withdraw(5) == None
    assert jar.withdraw(6) == ValueError
    assert jar.withdraw(-1) == ValueError
    
    
