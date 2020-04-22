#Author:xiaoai
#Time:2020/3/31 2:36 PM
import requests
import json
'''
url = "http://39.97.246.180:8889/login"
data1 = {"account": "zfb", "password": "111111"}
r = requests.post(url= url,data= data1)
global token
token = r.json()["data"]["token"]
assert r.status_code == 200
print(token)
print(r.status_code)
print(r.content)


url2 = "http://39.97.246.180:8889/v1/activity/list"
data2 = {"id": 0, "name": "", "type": 0, "bank_id": 0, "platform": 0, "status": 0, "page": 1, "count": 10}
headers2 = {"Authorization": token}
r2 = requests.post(url= url2,data= data2,headers= headers2)
print(r2.status_code)
print(r2.content)

ls = ["11","dd","小迷糊","2048"]
print(len(ls))
print(ls[0],"最后一位",ls[len(ls)-1],"或者change",ls[-1])

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print("我是输出的Apple",L[0][0])
print("我是输出的Python",L[1][1])
print("我是输出的Lisa",L[2][2])

arr  = [90,323,12,33,42,4,666,2,111,234,111,246]
n = len(arr)
for i in range(n):
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)
print("接下来进行数据类型转换======")
q1 = 10
q2 = .876j
q3 = 3.44443
print(int(q3))
print(complex(q1))
print(float(q1))
q4 = "update date"
print(q4[3:6])

q5 = ["wo","except","M","up","Python"]
print(len(q5))
print(max(q5))
print(q5.count("M"))

def goodg(age,heigth,weight):
    if age > 0 and heigth > 60 and weight < 25:
        print("that's perfect！")
chilli = goodg(0.1,80,20)

# lambda 函数语法：
# lambda [arg1 [,arg2,......argn]]:expression
sum = lambda arg1,arg2 : arg1 * arg2
print("计算所得：",sum(10,20))

ls  = [1,2,3,45,333,3432]
print(ls.index(2)) # 根据索引查找
ls.sort() # 排序
print(ls)
ls.reverse() # 倒排
print(ls)
ls.copy() # 复制
print(ls)
ls.append("追加一个哈哈") # 追加
print("====追加成功====",ls)
ls.insert(2,"我是一些内容") # 插入
print(ls)
print(ls.count(2)) # 统计某一元素的出现次数
ls.remove(2) # 删除
print(ls)
ls.pop(0) # 移除元素
print(ls)
# ls.clear() # 移除列表中的所有项
# print(ls)

from collections import deque
queue = deque(["Eric","john","Micheal"])
queue.append("cherry")
queue.append("strawberry")
print(queue)

file1 = "/Users/han/Desktop/test1.txt"
f1 = open(file1,"r")
print(f1.read())

while True:
    try:
        x = int(input("请输入一个数字"))
    except ValueError:
        print("您输入的并不是数字，请检查后重新输入！")
    else:
        print("这是错误的")
    finally:
        print("输入结束")


class people:
    age = 10
    name = "Lisa"
    __weight = 56
    def __init__(self,a,n,w):
        self.age = a
        self.name = n
        self.__weight = w
        print("我叫%s 今年%d岁 我的体重为%d公斤" %(n,a,w))

#a = people(12,"嘟嘟",4)
class chile(people):
    favorite = "Playing Compoter...."
    def __init__(self,a,n,w,f):
        people.__init__(self,a,n,w)
        self.favorite = f
        print("我叫%s 我最喜欢%s " %(n,f))
lili = chile(12,"LILI",23,"打篮球")

# 生成日历
import calendar
yy = int(input("输入年份："))
mm = int(input("输入月份"))
print(calendar.month(yy,mm))

ls4 = [33,44,2,54,26,80,8]
ls4.sort()
print(ls4[-1])

str = 'sunny'
#print(str[::-1])
#print(''.join(reversed(str)))

dic1 = {"a":200,"b":203,"c":219}
dic2 = {"e":"好好说话","b":"没有一些变化","c":219}
dic2.update(dic1)
print(dic2)
# sum  = 0
# for i in dic1:
#     sum = sum +dic1[i]
# print(sum)

# 字符串时间转时间戳
import time
a1 = "2020-04-08 11:00:00"
timeArray = time.strptime(a1,"%Y-%m-%d %H:%M:%S") #先转换为时间数组
timeStamp = int(time.mktime(timeArray)) #转换为时间戳
print(timeStamp)

# a2 = "2020/4/8 11:00:00"
# timeArray1 = time.strptime(a2,"%Y/%m/%d %H:%M:%S")
# otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S",timeArray)
# print(otherStyleTime)

import time
import datetime
# 先获得时间数组格式的日期
threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days=3))
# 转换为时间戳
timeStamp = int(time.mktime(threeDayAgo.timetuple()))
# 转换为其他字符串格式
otherStyletime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyletime)

l = list(range(100))
print(l)
print(l[::20]) # 间隔多少取一个值

# 30人在一条船上，超载需要15人下船，从1开始数，数到9的下船，循环留15人
# 30人的列表
my_list = []
for i in range(1, 31):
    my_list.append(i)
# 记录删除的人
del_ls = []
num = int(input("输入你要保留的人数："))
while True:
    if len(my_list) > num:
        ls = []
        for a in my_list:
            a1 = my_list.index(a)
            # 通过下标索引对9进行取整
            if (a1+1) % 9 == 0:
                ls.append(a)
                del_ls.append(a)
        for b in ls:
            if len(my_list) > num:
                my_list.remove(b)
            else:
                break
    else:
        print('留下来的人:', my_list)
        print("被删除的人：", del_ls)
        break
'''
print("\033[0m 默认字体终端输出")
print("\033[31;0m 红色字体终端输出")
print("\033[7;31;40m 高亮输出 \033[0m")
print("\033[1;32;40m 终端输出 \033[0m")
print("\033[1;31;40m 无背景输出 \033[0m")
