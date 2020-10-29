from program.not_string import not_string
import pytest

def test_not_string() :
    assert not_string( "with" ) == "not with"
    assert not_string( "not with" ) == "not with"