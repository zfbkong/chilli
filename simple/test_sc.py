#Author:xiaoai
#Time:2020/4/13 3:05 PM
'''
# fixture scope = "module" 可实现多个.py跨文件共享前置/ scope = "session" 可实现多个.py跨文件使用一个session来完成多个用例
# 实例一： fixture 参数传入（scope = "function"）
# 实现场景：用例1需要先登录，用例2不需要登录，用例3需要先登录
import pytest
# 不带参数时默认scope = "function"
@pytest.fixture()
def login():
    print("请输入账号，密码进行登录")

def test_s1(login):
    print("用例1：登录之后的其他操作11111")

def test_s2():
    print("用例2：无需登录，操作222222")

def test_s3(login):
    print("用例3： 登录之后其它动作3333333")

if __name__ =="__main__":
    pytest.main("-s","test_sc.py")
'''
import pytest
# scope = "module",module 作用是整个.py文件都会生效，用例调用时，参数写上函数名就行
@pytest.fixture(scope="module")
def open():
    print("打开浏览器，并且打开百度首页...")

def test_s1(open):
    print("用例1：搜索python-1")

def test_s2(open):
    print("用例2：搜索python-2")

def test_s3(open):
    print("用例3：搜索python-3")

if __name__ == "__main__":
    pytest.main("-s","test_sc.py")

