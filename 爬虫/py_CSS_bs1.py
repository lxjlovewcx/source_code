'''
Created on 2018年8月25日

@author: lixue
'''

'''
之前讲的的都是下载数据，
然后是提取数据，re，xlml库，xpath
现在使用数据提取中的一个很重要的工具。beautifulsoup4 ，本质是一个css选择器。
一旦使用，相当于将整个文档加载到内存中，这样会导致性能存在问题，因为占内存啊。
具体选择哪种提取数据的方法，需要根据文档的结构来进行选择
现在使用的是beatifulsoup4 
http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/
几种常用提取信息工具的比较：
        —正则：很快，不好用，不需安装
        -beatifulsoup：慢。使用简单，安装简单
        -lxml：比较快，使用简单，安装一般
'''
from urllib import request
from bs4 import BeautifulSoup
url = "http://www.baidu.com"

rsp =request.urlopen(url)
print(type(rsp))
content = rsp.read()
soup = BeautifulSoup(content,'lxml')
#bs制动转码
content =soup.prettify()
print(content)
