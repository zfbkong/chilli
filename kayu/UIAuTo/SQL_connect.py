#Author:xiaoai
#Time:2020/1/17 5:31 PM
import pymysql
db = pymysql.connect(host='rm-2ze3r1r45zex72x8bao.mysql.rds.aliyuncs.com',user='kayuwangluo',password='!yBW&6@*A&K',port='3306')
cursor = db.cursor()
cursor.execute("show databases")
results = cursor.fetchall()
print(results)
