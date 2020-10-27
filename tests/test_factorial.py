#test to check whether factorial function works
#This function should return 1 if x equals 0
#Otherwise, it should multiply x by factorial of x-1

import pytest
import factorial

def test_fact_zero() :
    assert factorial.fact( 0 ) == 1

def test_fact_nonzero() :
    assert factorial.fact( 6 ) == 720
