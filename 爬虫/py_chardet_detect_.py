'''
Created on 2018年8月17日

@author: lixue
'''
from urllib import request
import chardet
help(chardet)

if __name__ == '__main__':
    url = "http://www.eastmoney.com/"
    rsp = request.urlopen(url)
    html = rsp.read()
    cs = chardet.detect(html)
    print(cs)
    print(type(cs))
    html = html.decode(cs.get("encoding","utf-8")) #使用get保证其不会报错
    print(html)
#     print(html)
    #使用 chardet自动检测
    
    