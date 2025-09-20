import pytest
from seasons import scribe

def test_scribe_accuracy():
    assert scribe(1000) == "One thousand"
    assert scribe(1440) == "One thousand, four hundred forty"
