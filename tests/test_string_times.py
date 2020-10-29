from program.string_times import string_times
import pytest

def test_string() :
    assert string_times( 'lollipop', 2 ) == 'lollipoplollipop'
