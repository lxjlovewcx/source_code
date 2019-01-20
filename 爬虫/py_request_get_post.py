'''
Created on 2018年8月18日

@author: lixue
'''

'''
request.data 的使用
 -访问网络的两种方式
    -get：
        利用参数给服务器传递信息
        参数为dict，然后用parse编码
    -post
        -一般向服务器传递参数使用
        -post是把信息自动加密处理
        -我们如果想使用post信息，需要用到data参数
        -使用post，意味着http的请求头部可能需要更改：
            -content—type：
            —content—length：数据长度
            -简而言之，一旦更改请求方法，请注意其他请求头部信息相适应
            -urllib.parse.urlencode
'''
'''
利用parse模块模拟post请求
分析百度词典
    1：打开f12
    2：尝试输入girl，发现没敲一个字母后都有请求
    3：请求地址为：
    4：利用network 查看头部信息和body信息
    5：检查返回内容格式，发现返回的是json格式内容-需要用到json包——说明这是一个ajax请求
    
'''
from urllib import request,parse
import json
'''
大致流程
1：利用data构造内容，然后urlopen打开
2：返回一个json格式的结果
3：结果应该是gril的释义
'''
baseurl = 'http://fanyi.baidu.com/sug'
data = {
    'kw' : 'girl'
}
data = parse.urlencode(data).encode()
print(type(data))#<class 'bytes'>
'''
我们需要构造一个请求头，请求头部应该至少包含传入的数据的长度
request 要求传入的请求头是一个dict格式
请求头很重要，比如隐藏身份
有了headers，data，url，就可以发送请求了
'''
headers = {
    'content-length:len(data)'
}
rsp = request.urlopen(baseurl, data = data)
print(rsp)
json_data = rsp.read().decode()
print(type(json_data))#<class 'str'>
print(json_data)
json_data = json.loads(json_data)
print(type(json_data))
print(json_data)

for item in json_data['data']:
    print(item['k'] + ':'  + item['v'])
