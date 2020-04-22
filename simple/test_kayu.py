#Author:xiaoai
#Time:2020/4/13 5:02 PM
import pytest
import requests
class TestCases:
    token = ""
    # 登录
    def test_login(self):
        url = "http://39.97.246.180:8889/login"
        data1 = {"account": "zfb", "password": "111111"}
        r = requests.post(url=url, data=data1)
        global token
        token = r.json()["data"]["token"]
        assert r.status_code == 200
        print(token)
        print(r.status_code)
        print(r.content)

    # 查看活动管理列表
    def test_activityManager(self):
        url2 = "http://39.97.246.180:8889/v1/activity/list"
        headers2 = {"Authorization": token}
        dada2 = {"id":0,"name":"","type":0,"bank_id":0,"platform":0,"status":0,"page":1,"count":10}
        r2 = requests.post(url= url2,headers= headers2,data= dada2)
        assert r2.status_code == 200
        print(r2.status_code)
        print(r2.content)


if __name__ == "__main__":
    pytest.main("-s","test_kayu.py")





