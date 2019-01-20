'''
Created on 2018年8月17日

@author: lixue
'''
'''
enumerate
这个往数据库中丢东西比zip还要多
跟zip功能有点像
对可迭代对象中的每一额元素，配上一个索引，然后索引和内容构成tuple类型
'''
l1 = [11,22,33,44,55]
em = enumerate(l1)
print(type(em))#<class 'enumerate'>
print([i for i in l1])#[11, 22, 33, 44, 55]

em = enumerate(l1,start=100)#序列号从100开始
print([i for i in em])#[(100, 11), (101, 22), (102, 33), (103, 44), (104, 55)]