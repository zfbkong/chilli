#Author:xiaoai
#Time:2020/1/10 2:27 PM
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Firefox(executable_path="/Users/han/Downloads/geckodriver")
driver.maximize_window()
# 设置浏览器大小
#driver.set_window_size(800,600)
sleep(2)
driver.get('http://192.168.200.119:8080/#/')
# 登录
driver.find_element_by_class_name("el-input__inner").send_keys(u"zfb")
sleep(2)
driver.find_element_by_xpath("//*[@type='password']").send_keys(u"klklkl0000")
sleep(2)
driver.find_element_by_xpath("//*[@type='button']").click()
print("======进入卡与生活后台管理系统成功======")
sleep(3)

# 根据活动状态进行搜索
driver.find_element_by_xpath("//*[@placeholder = '请选择活动状态']").click()
print("======活动状态选择框下拉完成======")
sleep(2)
# 选择活动状态
driver.find_element_by_xpath("//span[text() = '上架']").click()
print("======活动状态选择完成======")
sleep(2)

# 点击"搜索"
# 根据类型定位按钮
# driver.find_element_by_xpath("//*[@type= 'button']").click()
driver.find_element_by_xpath("//span[text() = '搜索']").click()
print("======搜索完成======")

# 点击"banner"
driver.find_element_by_xpath("//span[text() ='banner']").click()
print("======进入banner列表成功======")
# 点击"申请管理"
sleep(2)
driver.find_element_by_xpath("//span[contains(text(),'申请管理')]").click()
print("======进入申请管理成功======")
sleep(2)
# 点击"卡版管理"
driver.find_element_by_xpath("//span[text() = '卡版管理']").click()
print("======进入卡版管理成功=====")
sleep(2)
# 点击"意见反馈"
driver.find_element_by_xpath("//span[text() = '意见反馈']").click()
print("======进入意见反馈成功======")
sleep(2)
# 点击"招聘申请"
driver.find_element_by_xpath("//span[text() = '招聘申请']").click()
print("======进入申请管理成功======")
sleep(2)
# 点击"订单管理"
driver.find_element_by_xpath("//span[text() = '订单管理']").click()
print("======进入订单管理成功======")
sleep(2)
# 滑动列表内容
js ="var q=document.documentElementTop=4500"
driver.execute_script(js)
sleep(2)
print("======滑动成功======")
'''
# 点击"投诉管理"
driver.find_element_by_xpath("//span[text() = '投诉管理']").click()
print("======进入投诉管理成功======")
sleep(2)
# 点击"关系网管理"
driver.find_element_by_xpath("//span[text() = '关系网管理']").click()
print("======进入关系网管理成功======")
sleep(2)
# 点击"银行管理"
driver.find_element_by_xpath("//span[text() = '银行管理']").click()
print("======进入银行管理成功======")
sleep(2)
# 点击"消息推送"
driver.find_element_by_xpath("//span[text() = '消息推送']").click()
print("======进入消息推送成功======")
time.sleep(2)
# 点击"操作日志"
driver.find_element_by_xpath("//span[text() = '操作日志']").click()
print("======进入操作日志成功======")
time.sleep(2)
print("======测试结束======")
driver.quit()
'''



















