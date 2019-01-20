'''
Created on 2018年8月25日

@author: lixue
'''
'''
css选择器
    -使用soup。select，返回一个列表
    -通过标签名称;soup.select("title")
    -通过class类名：soup。select（“。content”）
    -id查找：soup。select（“#name_id”）
    -组合查找：soup.select("div #input_content")
    -属性查找：soup.select(img[class='photo'])
    -获取tag内容：tag.get_text
'''
from urllib import request
from bs4 import BeautifulSoup
import re
url = "http://www.baidu.com"

rsp =request.urlopen(url)
print(type(rsp))
content = rsp.read()
soup = BeautifulSoup(content,'lxml')
print(soup)
print(soup.title)
tags = soup.find_all(re.compile)