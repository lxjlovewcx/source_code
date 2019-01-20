'''
Created on 2018年8月18日

@author: lixue
'''
'''
错误处理
在访问互联网的时候回遇到各种各样的问题，错误
urllib.error
    -URlError产生的原因：
        -没网
        -服务器链接失败
        -找不到指定的服务器
        -是属于OSError的子类
    -HTTPError产生的原因
        -
    两者之间的区别在哪里？
    HTTPError是对应的HTTP请求的返回码错误。4或者5的错误。
    URLError是对应的网络出现的问题，包括url问题。
        关系是：OSError-URLError-HTTPError
'''
from urllib import request,error
import json

if __name__ == '__main__':
    url = "http://fanyisddd.baidu.com/sug"
    try:
        req = request.Request(url)
        res = request.urlopen(req)
        html = res.read().decode()
        print(html)
        print(type(html))
        json_html = json.loads(html)
        print(json_html)
        print(type(json_html))
    except error.HTTPError as h:
        print("HTTPError :{0}".format(h))
    except error.URLError as e:
        print("URLError : {0}".format(e))
    except Exception as E:
        print(E)
'''
HTTPError是属于URLError的子类
'''

    