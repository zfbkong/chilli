#Author:xiaoai
#Time:2020/4/20 12:03 PM
import requests
# 方法一
'''
def send_request(method, url, request_data = None, headers = None):
    if method == "get":
        r = requests.get(method, url ,params = request_data, headers = headers )
    elif method == "post":
        r = requests.post(method, url, data = request_data, headers = headers)

    else:
        r = None
'''
# 方法二
def send_get(url, data):
    r = requests.get(url = url, params = data)
    result = r.json()
    return result

def send_post(url, data):
    r = requests.get(url = url, data = data)
    result = r.json()
    return result

def main(url, method, data):
    if method == "POST":
        r = send_post(url, data)
    else:
        r = send_get(url)










