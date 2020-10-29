from program.decorator_demo import hello
import pytest

def test_hello() :
    assert hello( "bonjour" ) == "BONJOUR"
    assert hello( "COOL" ) == "COOL"