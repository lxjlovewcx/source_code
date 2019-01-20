'''
Created on 2018年8月17日

@author: lixue
'''
from collections import namedtuple
'''
    -namedtuple 类
    -deque 类

namedtuple
    -tuple类型
    -是一个可命名的tuple
'''
help(namedtuple)

point = namedtuple('point', ['x','y'])#就是一个没有函数的类嘛，定义一个point的类
p = point(11,22)#实例化
print(point.__doc__)#point(x, y)
print(p.x) #11#实例化的属性
print(p[0])#11#由于返回的是一个tuple，因此可以使用索引

circle = namedtuple('circle', ['x','y','r'])#定义一个circle的类
c = circle(100,150,50)
print(c)
print(type(c))

print(isinstance(c, tuple)) #发现其属于tuple的子类
