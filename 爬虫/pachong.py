'''
Created on 2018年8月17日

@author: lixue
'''
from IPython.core.release import url
from ipywidgets.widgets.widget_link import jsdlink
from xml.etree.ElementPath import xpath_tokenizer
import xml
'''
爬虫准备工作
    -参考资料
        -python网络数据采集
    -精通python爬虫框架scrapy，人民邮电出版社
    -python3网络爬虫（http：//blog.csdn.net）
    -scrapy 官方教程
-前提知识
    -url
    -http协议
    -web前端，html，css，js
    -ajax
    -re，xpath
    -xml
1:爬虫简介
    按照一定规则，自动抓取万维网信息的程序或者脚本。
    另外一些不常使用的名字还有蚂蚁、自动索引、模拟程序或者蠕虫
- 两大特征
    -能按作者要求下载数据或者内容
    -能自动在网络上流窜
2:爬虫的三大步骤
    -下载信息
    -提取正确的信息
    -根据一定规则自动跳转到另外的网页上执行上两步内容
3:爬虫分类
    -通用爬虫
    -专用爬虫（聚焦爬虫） 使用爬虫工具专门干一件事情
4：python中爬虫会用到什么东西？
    -python网络包简介
    -python2：urllib，urllib2，urllib3，httplib，httplib2，requests
    -python3：urllib，urllib2，httplib2，requests
    -python2：urllib和urllib2配合使用，或者request
    -python3：urllib和requests
'''
    