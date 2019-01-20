'''
Created on 2018年8月16日

@author: lixue
'''
import datetime
import time
from _ast import In
print(datetime.date)#<class 'datetime.date'>
t = datetime.date(2018,3,26)#
#datetime 提供year.month,day 属性
print(t)#2018-03-26
print(t.day)#26
print(t.month)#3
print(t.year)#2018
#datetime.time()
#datetime.datetime
#datetime.timedelta:提供一个时间差，时间长度
from datetime import datetime,timedelta#datetime.datetime 提供日期与时间的组合
#常用的类方法：
#today
#now
#utcnow
#fromtimestamp：从时间搓中返回本地时间
dt = datetime(2018,8,15)
print(dt.today())
print(dt.now())

print(dt.fromtimestamp(time.time()))


#timedate.timedelta
# 表示一个时间间隔

t1 = datetime.now()
print(t1.strftime("%Y-%M-%d %H:%M:%S"))#对时间进行格式化
td = timedelta(hours = 1)#表示一小时的时间长度
print((t1+td).strftime("%Y-%M-%d %H:%M:%S"))#时间原时间再加上时间间隔后再格式胡输出

#timeit -时间测量工具
#测量程序运行时间间隔
def p():
    time.sleep(2)
t1 = time.time()
p()
print(time.time()-t1)

#列表生成方法的两种比较
#如果单纯比较生成一个列表的时间，可能很难实现
import timeit #测量程序运行时间
c = '''
list = []
for i in range(1000):
    list.append(i)
'''
#利用timeit调用代码，执行100000次，查看运行时间 比较下面连个函数的运行时间
t1 = timeit.timeit(stmt="[i for i in range(1000)]",  number = 10000)
t2 = timeit.timeit(stmt= c, number= 10000)   
print(t1)
print(t2)

help(timeit.timeit)

#timtit 可以执行一个程序，获取其

def doIt():
    num =3
    for i in range(num):
        print("repeat for {}".format(i))
t = timeit.timeit(stmt= doIt,number = 10)
print(t)

s = '''   
def doIt(num):
    for i in range(num):
        print("repeat for {}".format(i))
'''
t = timeit.timeit("doIt(num)",setup =s+"num=3",number = 10)#setup负责把环境变量配置好
'''
实际上相当于个timeit常见了一个小环境
执行顺序是
def doIt(num):
    for i in range(num):
        print("repeat for {}".format(i))
num = 3
doIt(num)
'''

print(t)

#datetime.datetime 模块  提供比较好用的时间而已
