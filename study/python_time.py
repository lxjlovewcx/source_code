'''
Created on 2018年8月16日

@author: lixue
'''
import time
from pygments import style
print(time.timezone)  # 时间模块的属性-28800
# 当前时区和utc时间相差的秒数
print(time.altzone) #有夏令时的时候-32400
print(time.time()) #时间戳1534410604.1171799
print(time.localtime()) #当前时间的时间结构time.struct_time(tm_year=2018, tm_mon=8, tm_mday=16, tm_hour=17, tm_min=10, tm_sec=4, tm_wday=3, tm_yday=228, tm_isdst=0)
t = time.localtime()
print(t.tm_year) #显示时间结构中的一个元素2018
tt = time.asctime(t) #返回元祖的正常字符串后的时间格式
print(tt)#Thu Aug 16 17:10:04 2018
print(type(tt))#<class 'str'>
tt = time.mktime(t)#获取指定时间节点的时间戳
print(tt)
print(type(tt))#<class 'float'>

#clock：获取cpu时间，比如测试程序运行的时间。
for i in range(10):
    print(i)
    time.sleep(0)   #休息时间
    
def p():
    time.sleep(2.5)
t1 = time.clock()
print(t1)#4.2765234259400226e-07
p()
t2 = time.clock()  #获取当前cpu时间
print(t2-t1)#2.5037470898258087

t= time.localtime()
print(type(t))
ft = time.strftime(t)
print(time.ctime())

