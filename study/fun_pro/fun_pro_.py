'''
Created on 2018年8月16日

@author: lixue
'''
from builtins import map
'''
高阶函数
    把函数作为参数使用的函数
变量可以赋值
    函数名称就是一个变量
'''
#证明函数名称就是一个变量
def funA():
    print("funA Hello")
print(funA)#funA是一个变量，其值为<function funA at 0x02F934B0>
print(funA())#执行funA中的程序，但是无返回值默认为none。

funB=funA#将特殊的函数变量赋值给funB
funB()#funA Hello

'''
函数名是变量
funB和funA指向同一片代码
既然函数名称是变量，则应该可以被作为参数传入另一个函数

'''
# 普通函数
def funC(n):
    return n *100
def funB(n):
    return funC(n) *3
print(funB(9))

#高阶函数
def funD(n,f):
    return f(n) *3
print(funD(9, funC))
#从上可知，使用高阶函数闲的更加灵活，多变
'''
系统高阶函数-map
- 愿意就是映射，即把集合或者列表的元素，每一个元素都按照一定规则进行操作，生成一个新的列表或者集合
-map函数时系统提供的具有映射功能的函数，返回值是一个迭代对象。

python2和python3的却别在map函数这个上，python2里处理的数据时什么类型，map玩后还是那个类型
而在python3中不管可迭代独享是什么类型，结果都是map类型
'''
l1 = [i for i in range(10)]
print(l1)
l2 = []
for i in l1:
    l2.append(i*10)
print(l2)


#利用map实现
def multen(n):
    return n*10
rst = map(multen,l1)
print(rst)

for i in rst:
    print(i,end=",")
    
print(type(rst))
ss = [i for i in rst]
print(type(ss))
print(ss)

'''
reduce 
    -愿意是归并，缩减
    -把一个可迭代对象最后归并为一个结果
    -对于作为参数的匿名函数：必须由两个参数，必须由返回结果
'''
from functools import reduce
def funE(x,y):
    return x + y
rst = reduce(funE, [i for i in range(10)])
print(rst)