'''
Created on 2018年8月17日

@author: lixue
'''
from urllib import  request
if __name__ == '__main__':
    url = "http://www.eastmoney.com/"
    rsp = request.urlopen(url)
    print(type(rsp))#<class 'http.client.HTTPResponse'>
    print(rsp)#<http.client.HTTPResponse object at 0x03182AD0>
    html = rsp.read()
    print("url :{0}".format(rsp.geturl()))
    print("url info :{0}".format(rsp.info()))
#     print("url body: {0}".format(rsp.))
    print("url code:{0}".format(rsp.getcode()))
    
'''
rsp 是一个实例，那么实例下面有哪些方法呢？
rsp.geturl()
rsp.info()
rsp.getcode()
'''   