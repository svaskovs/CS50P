import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/2") == 50
    assert convert("99/100") == 99
    assert convert("1/100") == 1
    assert convert("0/100") == 0

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_error_value():
    with pytest.raises(ValueError):
        convert("3/2")

def test_error_zero():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")
