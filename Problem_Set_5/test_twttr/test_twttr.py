from twttr import shorten

def test_shorten_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("hello, world") == "hll, wrld"
    assert shorten("aeiou") == ""

def test_shorten_upper():
    assert shorten("twIttEr") == "twttr"
    assert shorten("HELLO, WORLD") == "HLL, WRLD"
    assert shorten("AEIOU") == ""

def test_shorten_special():
    assert shorten("tw1tt3r") == "tw1tt3r"
    assert shorten("hell@,_w$rld!!!") == "hll@,_w$rld!!!"
    assert shorten("@#iou") == "@#"

def test_shorten_noInput():
    assert shorten("") == ""
    