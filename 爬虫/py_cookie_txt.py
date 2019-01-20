'''
Created on 2018年8月19日

@author: lixue
'''
'''
创立handler后，使用operer打开，打开后响应的业务由响应的handler处理
-cookie作为一个变量，打印出来
    -cookie的属性
        -name：名称
        -value：值
        -domain：可以访问此cookie的域名
        -path：可以发送此cookie的页面路径
        -expire：过期时间
        -size：大小
        -http：字段
    理论上将不能修改cookie的值，也没用，安全机制为两份，cookie不行session也要看。
cookie保存在内存里，作为一个变量存在。

-cookie的保存