'''
Created on 2018年8月25日

@author: lixue
'''
from urllib import request
from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString, Comment
'''
BeautifulSoup 四大对象
    -Tag
    -NavigableString
    -beatifulsoup
    -Comment
-tag    
    -对用html中的标签
    -可以通过soup.tag_name
    -tag连个重要的属性，name,attrs
-navigablestring
    -对应内容值
-beatifulsoup 
    -表示一个文档的内容，大部分可以把它当成tag对象
    -一般我们可以用手soup表示
-comment
    -特殊类型的navagablestring对象
    -对其输出，则内容不包括注释符号
    
    只是寻找第一个标签
'''
url = "http://www.baidu.com"

rsp =request.urlopen(url)
print(type(rsp))
content = rsp.read()
soup = BeautifulSoup(content,'lxml')
#bs制动转码
content =soup.prettify()
print(content)
print("==" * 12)
print(soup.head)
print("==" * 12)
print(soup.meta)
print("==" * 12)
print(soup.link)
print("==" * 12)
print(soup.link.name)
print("==" * 12)
print(soup.link.attrs)
print(soup.link.string)
print(soup.title.string)
print("==" * 12)
print(soup.link.attrs['type'])
print("==" * 12)
print(soup.name)
print(soup.attrs)
print(soup.string)

