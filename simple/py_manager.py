import pytest
import time
def test_one():
    time.sleep(3)

if __name__ == '__main__':
    #pytest.main(['-q', 'py_test10']) #方式一
    pytest.main("-s","py_test10") # 方式二
