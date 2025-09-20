import pytest
from working import convert

def test_convert_am():
    assert convert("1:00 AM to 2:00 AM") == "01:00 to 02:00"
    assert convert("12:00 AM to 11:00 AM") == "00:00 to 11:00"
    assert convert("1:30 AM to 4:59 AM") == "01:30 to 04:59"

def test_convert_pm():
    assert convert("1:00 PM to 2:00 PM") == "13:00 to 14:00"
    assert convert("12:00 PM to 11:00 PM") == "12:00 to 23:00"
    assert convert("1:30 PM to 4:59 PM") == "13:30 to 16:59"

def test_convert_noMin():
    assert convert("9 AM to 11 AM") == "09:00 to 11:00"
    assert convert("9:30 PM to 11 PM") == "21:30 to 23:00"
    assert convert("12 AM to 12:59 PM") == "00:00 to 12:59"

def test_convert_format():
    with pytest.raises(ValueError):
       convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 13:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 to 1:00 PM")
    with pytest.raises(ValueError):
        convert("0:00 AM to 24:00 PM")
