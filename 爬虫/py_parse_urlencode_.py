'''
Created on 2018年8月17日

@author: lixue
'''
from urllib import request,parse
'''
网络的访问一个是get和post，向服务器传送数据。
'''
if __name__ == '__main__':
    base_url = "http://www.baidu.com/s?"
    wd = input("input your keyword:")
    
    qs = {
        "wd":wd
    }
    
    qs = parse.urlencode(qs)#是一个字典，先对输入的数据进行编码
    fulurl = base_url + qs
    print(fulurl)
    rsp = request.urlopen(fulurl)
    print(rsp)
    html = rsp.read()
    html = html.decode("utf-8")
    print(html)
    
    