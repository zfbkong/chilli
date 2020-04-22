#Author:xiaoai
#Time:2019/11/29 4:32 PM
import pytest
def func(x):
    return x+1

def test_answer():
    assert func(5) == 4

if __name__ == '__main__':
    pytest.main(["-q","test.py"])