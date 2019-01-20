'''
Created on 2018年8月18日

@author: lixue
'''
'''
为了设置更多的信息，比如headers，我们使用request.Request
Request这个类用于添加headers参数
'''
from urllib import request,parse
import json

baseurl = 'http://fanyi.baidu.com/sug'
data = {
    'kw' : 'girl'
}

data = parse.urlencode(data).encode()
headers = {
    'content-length':len(data)
}

rsp = request.Request(url=baseurl, data=data, headers=headers)#构造一个request的实例
data = request.urlopen(rsp)
print(data)
json_data = data.read().decode()
json_data = json.loads(json_data)
print(json_data)
for item in json_data['data']:
    print(item['k'], '...' ,item['v'])



