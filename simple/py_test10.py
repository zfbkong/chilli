#Author:xiaoai
#Time:2020/4/10 11:25 AM
# 在python代码中调用pytest 调用方式pytest.main()
import pytest
import requests
import time
class TestCases:
    def setup(self):
        print(" 每个用例开始前都会执行...")

    def teardown(self):
        print(" 每个用例结束后都会执行...")
    # 实例一
    def test_one(self):
        print("====正在执行...")
        time.sleep(3)

    # 实例二
    def test_two(self):
        print("====正在执行...")
        url = "http://39.97.246.180:8889/login"
        data1 = {"account": "zfb", "password": "111111"}
        r = requests.post(url=url, data=data1)
        global token
        token = r.json()["data"]["token"]
        assert r.status_code == 200
        print(token)
        print(r.status_code)
        print(r.content)

if __name__ == '__main__':
    #pytest.main(['-q', 'py_test10']) #方式一
    pytest.main("-s","py_test10") # 方式二



