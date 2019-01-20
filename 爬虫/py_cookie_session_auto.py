'''
http模块包含一些关于cookie的模块，通过他们我么可以自动使用cookie
    -CookieJar  
        -管理存储cookie，向传出的http请求添加cookie
    -FileCookieJar(filename,delayload=None，policy=None):
        -使用文件管理cookie
        -filename是保存cookie的文件
    -MozillaCookieJar(filename,delayload=None，policy=None):
        -创建于mocilla浏览器cookie。txt兼容的FileCookieJar实例
    -LwpCookieJar(filename,delayload=None，policy=None):
        -创建于lib
-利用cookiejar访问人人，
    -自动使用cookie登录，大致流程是：
    -
'''
from urllib import request,parse
from http import cookiejar
#创建cookiejar的实例
cookie = cookiejar.CookieJar()
#生成cookie的管理器
cookie_handles = request.HTTPCookieProcessor(cookie)
#创建http请求管理器
http_handles = request.HTTPHandler()
#生成https管理器
https_handle = request.HTTPSHandler()
#创建请求管理器
opener = request.build_opener(http_handles,https_handle,cookie_handles)

def login():
    '''
    负责初次登录
    
