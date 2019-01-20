'''
Created on 2018年8月25日

@author: lixue
'''
'''
遍历文档对象
    -contents:tag的子节点以列表的方式输出
    -children：子节点以迭代器形式返回
    -descendants：用子孙遍历
    -string
搜索文档对象
    -find_all(name,attrs,recursive,text,** kwargs)
        -name；按照那个字符串搜索，可以传入的内容为
            -字符串
            -正则表达式
            -列表
        -keyword参数，可以用来表示属性
        -text:对应
'''
from urllib import request
from bs4 import BeautifulSoup
url = "http://www.baidu.com"

rsp =request.urlopen(url)
print(type(rsp))
content = rsp.read()
soup = BeautifulSoup(content,'lxml')
#bs制动转码
print(soup.name)
print("==="*12)
# for node in soup.head.contents:
#     if node.name == "meta":
#         print(node)
#     if node.title == "":


       
