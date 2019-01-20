'''
Created on 2018年8月19日

@author: lixue
'''
from http.cookiejar import Cookie
'''
源于http协议的无状态，无响应。
http协议是互联网的及时，目前的数据爬取都是基于http协议的。
http协议的记不住人，或者说是老年痴呆症。
每次访问的时候，服务器给一个凭证，
由于cookie发给客户端的不安全性（其他人都可以更改）。因此还需要发给服务器一个凭证。只有这两个合上了，就可以信任了。

由于http协议的无记忆性，人们为了你补这个缺陷，所采用的一个补充协议。
cookie是发给用户的（http浏览器）的一段信息，session是保存在服务器的对应的另一半信息，用来记录用户信息。

    -cookie和session的区别
        -存放位置不同
        -cookie不安全，主要保存身份验证，其他重要信息放在session部分中。处于安全考虑，都让其有一个过期的时间，而且保村太多会影响服务器的性能因此有定期淘汰机制。
        -session 会保存在服务器上一定时间，过期时间相对很短
        -单个cookie保存数据不超过4k，很多浏览器限制一个站点最多保存20个。
    session的存放位置
    -存在服务器端
    -一般情况，session是放在内存中或者数据库中的，一般由框架自动处理的，因此要创建数据库，如果没有数据库，一挂session就崩溃。
    '''
    
'''
    Cookie登录
   因为在本地浏览器中存在cookie，因此使用哪个网站能够登录上。
       '''


'''
没有cookie登录
'''

# from urllib import request
# if __name__ == '__main__':
#     url = "http://www.renren.com/965187997/profile"
#     rsp = request.urlopen(url)
#     print(rsp.read().decode())
'''
有cookie登录
'''
from urllib import request
if __name__ == '__main__':
    url = "http://www.renren.com/965187997/profile"
    headers = {
        "Cookie" : "anonymid=jkzocrpcz24fir; depovince=GW; jebecookies=c1ca835f-5501-4983-ad49-002fdb20fa3c|||||; _r01_=1; JSESSIONID=abcfjSPBLeMSTfOSjaovw; ick_login=f4e4613d-4c93-4484-975b-297ec192f228; jebe_key=f279caa6-b1e7-4314-a79d-f9f2cd502e43%7Cb8cfb23cd9624f4b076565d7d5c51635%7C1534612039295%7C1%7C1534612044927; t=b2ccd5450c2327d5e2d70b061d1351f29; societyguester=b2ccd5450c2327d5e2d70b061d1351f29; id=967607359; xnsid=b1feac74; wp_fold=0"
        }
    req = request.Request(url,headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    with open("rsp.html","w") as f:
        f.write(html)