#Author:xiaoai
#Time:2020/4/15 2:09 PM
import unittest
import requests
from HTMLTestRunner import HTMLTestRunner
class Kayu(unittest.TestCase):
    token = ""
    # 登录用例
    def test1_Login(self):
        url = "http://39.97.246.180:8889/login"
        data1 = {"account": "zfb", "password": "111111"}
        r = requests.post(url=url, data=data1)
        global token
        token = r.json()["data"]["token"]
        assert r.status_code == 200
        print(token)
        print(r.status_code)
        print(r.content)

    # 获取活动列表用例
    def test2_ActivityList(self):
        url2 = "http://39.97.246.180:8889/v1/activity/list"
        headers2 = {"Authorization": token}
        dada2 = {"id": 0, "name": "", "type": 0, "bank_id": 0, "platform": 0, "status": 0, "page": 1, "count": 10}
        r2 = requests.post(url=url2, headers=headers2, data=dada2)
        assert r2.status_code == 200
        print(r2.status_code)
        print(r2.content)

if __name__ == "__main__":
    # 创建测试集
    suite = unittest.TestSuite()
    # 添加测试用例到测试集
    suite.addTest(Kayu("test1_Login"))
    suite.addTest(Kayu("test2_ActivityList"))
    # 普通运行方式
    #unittest.main()
    #生成测试报告 给html命名并设置所在位置
    report_file = "/Users/han/PycharmProjects/untitled3/kayu/kayu_report.html"
    # 打开文件
    fp = open(report_file,"wb")
    # 添加报告的标题和描述信息
    runner = HTMLTestRunner(stream = fp, title = "卡与生活测试报告", description = "这是后台管理接口相关的测试内容")
    runner.run(suite)




