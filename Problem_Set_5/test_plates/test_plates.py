from plates import is_valid

def test_is_valid():
    assert is_valid("HELLO") == True
    assert is_valid("HELLOO") == True
    assert is_valid("HELLOWORLD") == False
    assert is_valid("1HELLO") == False
    assert is_valid("HE110") == True
    assert is_valid("HE012") == False
    assert is_valid("HELL0") == True
    assert is_valid("HE-LLO") == False
    assert is_valid("H3LLO") == False