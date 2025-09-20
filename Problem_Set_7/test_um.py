from um import count

def test_count_simple():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    

def test_count_mult():
    assert count("Um, thanks, um...") == 2
    assert count("Um, not sure, the sum does't, um... add up um bummer") == 3
    assert count("Um, um, UM uM, um, UM") == 6

def test_count_noUm():
    assert count("No ums in this string, bummer...") == 0