'''
Created on 2018年8月18日

@author: lixue
'''
'''
useragent 用户代理
    -useragent:用户代理，简称UA，属于heads的一部分，服务器通过UA来判断用户的身份。
    -常见的UA值，使用的时候可以直接复制粘贴，也可以用浏览器访问的时候抓包
设置UA可以通过以下两种方式：
    1：使用headers
    2：使用add_header方法
'''
from urllib import request,error
import json
if __name__ == '__main__':
    try:
        url = "http://fanyi.baidu.com/sug"
        headers = {}
        headers['User-Agent'] = '1.0) Gecko/20100101'
        req = request.Request(url = url,headers=headers)
        res = request.urlopen(req)
        json_res = res.read().decode()
        json_res = json.loads(json_res)
        print(json_res)
        req = req.add_handler("User-Agent","1.0) Gecko/20100101")
    except error.HTTPError as h:
        print("HTTPError :{0}".format(h))
    except error.URLError as e:
        print("URLError : {0}".format(e))
    except Exception as E:
        print(E)
        
