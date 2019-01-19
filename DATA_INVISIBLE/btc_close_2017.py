try:
    from urllib2 import urlopen      #使用python2的导入下载模块
except ImportError:
    from urllib.request import urlopen  #使用python3的导入下载文件使用的模块

import json  #专门用于处理下载后的json文件

json_url = "https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"
respon = urlopen(json_url)  #通过urlopen打开网站响应的结果得到一个文件对象，
# <http.client.HTTPResponse object at 0x056CF750>
print(respon)
req = respon.read()  #返回一个二进制文本
print(req)
# 将数据写入文件
#Python文件使用“wb”方式打开，写入字符串会报错，因为这种打开方式为：以二进制格式打开一个文件只用于写入。
# 如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
with open('btc_close_2017_urllib.json', 'wb') as f:
    f.write(req)
#加载json格式,将json格式的转化为标准list格式，去掉其中的一些东西
#将其转换为python可以处理的格式
file_urllib = json.loads(req)
print(file_urllib)





