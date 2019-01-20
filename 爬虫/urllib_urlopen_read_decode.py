'''
Created on 2018年8月17日

@author: lixue
'''
import urllib
from urllib import request
print(type(urllib))#<class 'module'>
print(type(request))#<class 'module'>
'''
urllib
-包含模块
    -urllib.request:打开和读取urls ，打开url，把网页弄下来
    -urllib.error:包括urllib.request产生的常见错误，使用try捕捉
    -urllib.parse:包括解析url的方法
    -urllib.robotparse:解析robots.txt文件  机器人协议，（里面写明了哪些是乐意读取的，哪些是不乐意爬取的。）
    对网站频繁的访问，别人会有反爬虫工具，甚至把你的ip地址封掉

    '''
#案例
if __name__ == '__main__':
    rsp = request.urlopen("https://www.cnblogs.com/")
    #读取返回结果
    print(type(rsp))#<class 'http.client.HTTPResponse'>
    html = rsp.read()
    print(type(html))#<class 'bytes'>
    #如果想把bytes转化为字符串，需要解码
    html = html.decode("utf-8")
    print(type(html))#<!DOCTYPE html>
    print(html)
'''
网页编码问题解决
    -chardet 可以自动检测页面文件的编码格式，但是可能有误。程序在下载的文档中查找是否有编码格式，如果没有，就靠蒙了
'''
    
    
    
    
