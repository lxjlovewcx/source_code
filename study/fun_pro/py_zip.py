'''
Created on 2018年8月17日

@author: lixue
'''
from builtins import zip
from itertools import groupby
'''
补充几个高阶函数
zip
    -把两个可迭代内容生成一个可迭代的tuple元素类型组成的内容
往数据库丢数据经常用到
'''

l1 = [1,1,2,2,3,4,5,5]
l2 = [11,22,33,44,55,66,23,24]
z = zip(l1,l2) 
print(type(z))  #<class 'zip'>
#print([ i for i in z])#[(1, 11), (2, 22), (3, 33), (4, 44), (5, 55)]
for i, j in groupby(sorted(z), key=lambda _: _[0]):
    print(i,j)
    for k in j:
        print(k)
 #   y_list = [v for v in j]
#    print(y_list)


help()
#help(groupby)
