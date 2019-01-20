'''
Created on 2018年8月17日

@author: lixue
'''
'''
高阶函数-排序
    -把一个序列按照给定算法排序
    -key参数：在排序前对每一个元素进行key函数云撒，可以理解为按照key函数定义的逻辑进行排序
    python2和python3差异很大
    '''
a = [1321,242,4,242,4,2,4,24234242,4,242,34,2424,2,4]
al = sorted(a)
print(al)

a= [-1234,-3242,232,34234,554,-543]
al = sorted(a,key = abs ,reverse = True)#按照绝对值进行排序
print(al)

abtr = ['dsf','sfdsgs','gsfsdfe','FSF', 'dfFSDF']
str1 = sorted(abtr)
print(str1)

str2 = sorted(abtr,key = str.lower)
print(str2)
