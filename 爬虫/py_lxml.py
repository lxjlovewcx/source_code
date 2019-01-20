'''
Created on 2018年8月25日

@author: lixue
'''
'''
lxml 库
python的HTML\XML 解析器
常用的解析器之一
官方文档：
使用：
'''
from lxml import etree
'''
用lxml解析HTML代码
'''
text = '''
<div>
    <url>
        <li class = "item-0"><a href="1.html">first item</a></li> 
        <li class = "item-0"><a href="1.html">first item</a></li>
        <li class = "item-0"><a href="1.html">first item</a></li>
        <li class = "item-0"><a href="1.html">first item</a></li>
        <li class = "item-0"><a href="1.html">first item</a></li>
    </url>
</div>
'''
html = etree.HTML(text)#解析生成html文档，可以修用html文档，把html缺的标签给你补全了
#读取文件
s = etree.tostring(html)
print(s)
#只能读取xml格式的内容，读取html文件格式的会报错。
xml = etree.parse("./v30.html")
rst = etree.tostring(xml,pretty print=True)
print(rst)
#结合xpath方法，完成文件查找
rst = html.xpath('//book[@category="sport"]')
print(rst.tag)
print(rst.context)

