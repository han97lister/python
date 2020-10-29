import pytest
from program.front_times import front_times

def test_front_times() :
    assert front_times( "Chocolate" , 2 ) == "ChoCho"
    assert front_times( "Ab" , 4 ) == "AbAbAbAb"