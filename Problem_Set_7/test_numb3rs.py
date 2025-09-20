import random
from numb3rs import validate

def test_validate_true():
    assert validate("1.1.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("255.255.255.0") == True
    assert validate("111.0.0.0") == True

def test_validate_false():
    assert validate("250.256.256.256") == False
    assert validate("111.cat.0.0") == False
    assert validate("111.000.000.000") == False
    assert validate("111.01.0.0") == False
    assert validate(" 111.0.0.0") == False
    assert validate("111.0.0.0 ") == False
    assert validate("111.0. 0.0") == False

def test_validate_random():
    assert validate(f"{random.randrange(0,9)}.{random.randrange(0,9)}.{random.randrange(0,9)}.{random.randrange(0,9)}") == True
    assert validate(f"2{random.randrange(0,5)}.{random.randrange(1,9)}{random.randrange(0,9)}.{random.randrange(1,9)}{random.randrange(0,9)}.{random.randrange(1,9)}{random.randrange(0,9)}") == True