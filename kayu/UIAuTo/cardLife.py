#Author:xiaoai
#Time:2019/12/17 3:10 PM
import os
import unittest
import time
from selenium.webdriver import android
from appium import webdriver

# 设备信息
desired_caps = {
    'device':'android',
    'platformName':'Android',
    'deviceName':'Redmi 4A',
    'platformVersion':'6.0.1',
    'appPackage':'com.cardandnetwork.cardandlife',
    'appActivity':'com.cardandnetwork.cardandlife.ui.activity.homeactivity.WelcomeActivity',
    'unicodeKeyboard':True,
    'resetKeyboard':True
}

class Login(unittest.TestCase):
    # 验证码登录
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    print("======安装成功=======")
    time.sleep(3)

    # 滑动欢迎页，进入系统
    def test1WelecomePage(self):
        x = self.driver.get_window_size("width")
        y = self.driver.get_window_size("height")
        print(x,y)
        # 滑动x*0.8,y*0.5,x*0.2,y*0.5
        self.driver.swipe(576,640,144,640)
        print("====滑动一次完成====")
        time.sleep(1)
        # 滑动到第三张欢迎页
        self.driver.swipe(576, 640, 144, 640)
        print("====滑动二次完成====")
        time.sleep(1)
        # 点击"立即体验"
        self.driver.find_element_by_xpath("//*[@text='立即体验']").click()
        print("=====进入系统成功====")
        time.sleep(1)
        '''
        # 由于获取验证码有一分钟的间隔限制，不适于验证码登录
        '''
        # # 输入手机号
        # self.driver.find_element_by_id("com.cardandnetwork.cardandlife:id/edit_phone").send_keys(u"13041201075")
        # #time.sleep(3)
        # # 获取验证码
        # self.driver.find_element_by_xpath("//*[@text='获取验证码']").click()
        # print("======进入获取验证码页成功======")

        # 切换至账号密码登录
        self.driver.find_element_by_id("com.cardandnetwork.cardandlife:id/btn_loginForPwd").click()
        time.sleep(1)
        # 输入手机号和密码
        self.driver.find_element_by_id("com.cardandnetwork.cardandlife:id/edit_phone").send_keys(u"13041201075")
        self.driver.find_element_by_id("com.cardandnetwork.cardandlife:id/edit_pwd").send_keys(u"klklkl0000")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@text='登录']").click()
        print("======登录成功======")
        time.sleep(1)


    def test2FirstPage(self):
        # 确认允许接受消息内容
        self.driver.tap([(600,1200)])
        print("======确认成功======")
        time.sleep(1)
        # 查看活动详情
        self.driver.tap([(520,365)])
        time.sleep(3)
        # 滑动查看详情内容
        self.driver.swipe(380,1200,380,750,200)
        print("======滑动完成======")
        time.sleep(3)
        # 向上滑动内容
        self.driver.swipe(380,750,380,1200)
        time.sleep(3)
        # 点击返回icon，返回首页
        self.driver.tap([(30,100)])
        print("======返回首页成功======")
        time.sleep(3)

    #
    # def test3ApplyCard(self):
    #     # 切换tab到"办卡"
    #     self.driver.find_element_by_xpath("//*[@text='办卡']").click()
    #     time.sleep(1)
    #     # 选择银行
    #     self.driver.tap([(99,620)])
    #     print("======心仪银行已选中======")
    #     time.sleep(3)
    #     # 选择卡版进行办理
    #     self.driver.tap([(520,250)])
    #     print("======进入卡版详情页======")
    #     time.sleep(1)
    #     # 点击"立即办理"
    #     self.driver.find_element_by_xpath("//*[@text='立即办理']").click()
    #     print("======进入填写资料页======")
    #     time.sleep(2)
    #     # 滑动到填写个人信息模块
    #     self.driver.swipe(400,1200,400,600)
    #     time.sleep(2)
    #     # 填写资料
    #     self.driver.find_element_by_id("com.cardandnetwork.cardandlife:id/fill_edit_name").send_keys(u"Chilli")
    #     print("======姓名填写完成======")
    #     time.sleep(1)
    #     self.driver.find_element_by_id("com.cardandnetwork.cardandlife:id/fill_edit_phone").send_keys(u"13041201075")
    #     print("======手机号填写完成======")
    #     time.sleep(1)
    #     # 下拉选择办理地区
    #     self.driver.find_element_by_id("com.cardandnetwork.cardandlife:id/fill_text_region").click()
    #     time.sleep(2)
    #     # 确认办理地区
    #     self.driver.find_element_by_id("com.cardandnetwork.cardandlife:id/btnSubmit").click()
    #     print("======办理地区选择完成======")
    #     time.sleep(2)
    #     self.driver.find_element_by_id("com.cardandnetwork.cardandlife:id/fill_edit_address").send_keys(u"木屋7788")
    #     print("======办理地址输入完成======")
    #     time.sleep(1)
    #     self.driver.find_element_by_id("com.cardandnetwork.cardandlife:id/fill_edit_companyName").send_keys(u"测试小分队")
    #     print("======公司名称输入完成======")
    #     time.sleep(1)
    #     # 滑动页面选择办理信息
    #     self.driver.swipe(400,1200,400,600)
    #     time.sleep(2)
    #     self.driver.tap([(200,700)])
    #     print("======拥有项选择完成======")
    #     time.sleep(2)
    #     # 提交资料
    #     self.driver.find_element_by_xpath("//*[@text='提交']").click()
    #     print("======办卡信息提交成功======")

    def test4UserPager(self):
        # 切换tab到我的
        self.driver.find_element_by_xpath("//*[@text='我的']").click()
        print("======成功进入我的页面======")
        time.sleep(1)
        # 查看个人信息
        self.driver.tap([(520,250)])
        print("======进入个人中心成功======")
        time.sleep(1)
        # 返回我的页面
        self.driver.find_element_by_id("com.cardandnetwork.cardandlife:id/titlebar_backImg").click()
        time.sleep(1)
        print("======返回成功======")
        # 查看订单列表
        self.driver.find_element_by_xpath("//*[@text='订单']").click()
        print("======进入订单列表成功======")
        time.sleep(2)
        # 切换tab～
        self.driver.find_element_by_xpath("//*[@text='待接单']").click()
        print("======切换tab至待接单成功======")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@text='已完成']").click()
        print("======切换tab至已完成成功======")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@text='已取消']").click()
        print("======切换tab至已取消成功======")
        time.sleep(2)
        # 返回我的页面
        self.driver.find_element_by_id("com.cardandnetwork.cardandlife:id/titlebar_backImg").click()
        print("======返回成功======")
        time.sleep(2)
        # 查看邀请注册
        self.driver.find_element_by_xpath("//*[@text='邀请注册']").click()
        print("======进入邀请注册页成功======")
        time.sleep(2)
        # 返回我的页面
        self.driver.find_element_by_id("com.cardandnetwork.cardandlife:id/titlebar_backImg").click()
        print("======返回成功======")
        # 进入意见反馈页
        self.driver.find_element_by_xpath("//*[@text='意见反馈']").click()
        print("======进入意见反馈页成功======")
        time.sleep(2)
        # 返回我的页面
        self.driver.find_element_by_id("com.cardandnetwork.cardandlife:id/titlebar_backImg").click()
        print("======返回成功======")
        time.sleep(2)
        # 进入联系客服页
        self.driver.find_element_by_xpath("//*[@text='联系客服']").click()
        print("======进入联系客服页成功======")
        time.sleep(2)
        # 返回我的页面
        self.driver.find_element_by_id("com.cardandnetwork.cardandlife:id/titlebar_backImg").click()
        print("======返回成功======")
        time.sleep(2)
        # 进入设置页面
        self.driver.find_element_by_xpath("//*[@text='设置']").click()
        print("======进入设置页面成功")
        time.sleep(2)
        # 退出登录
        self.driver.find_element_by_xpath("//*[@text='退出账号']").click()
        print("一切顺利，再见了伙计～")














if __name__ == '__main__':
    unittest.main()










