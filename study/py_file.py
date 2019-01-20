'''
Created on 2018年8月17日

@author: lixue
'''
import os
'''
长久保存信息的一种数据信息集合
常见操作 打开关闭（文件一旦打开，需要关闭操作）
读取内容
查找
'''
''' 
open 函数
    -open 函数负责打开文件，带有很多参数
    -第一个参数：必须有，文件的路径和名称
    -mode：表明文件用什么方式打开?
        -r: 以只读方式打开
        -w: 以写方式打开，会覆盖以前的内容
        -x :创建方式打开，如文件已经存在，报错
        -a：append方式，以追加的方式对文件内容进行写入
        -b：binary方式，二进制方式写入
        -t：文本方式打开
        -+:可读写
以写方式打开的文件必须关闭，以读方式打开的文件，关不关闭无所谓。
'''

#打开文件，用写的方式
#
#f称之为文件句柄
f = open(r"haha1.txt",'w')
#关闭文件
f.close()
#此案列说明，以写方式打开文件，默认是如果没有文件，则创建

'''
打开文件一般使用with语句较多。
with语句
    -with语句使用的技术是一种成为上下文管理协议的技术（contextmanagementprotocal）
    -自动判断文件的作用域，自动关闭不在使用的打开的文件句柄
'''
print(os.getcwd())
with open(r"haha1.txt", 'r') as f:
    pass
# 一下结构保证能够完整读取文件所有数据
with open(r"haha.txt", 'r') as f:
    strline = f.readline()
    while strline:
        print(strline)
        strline = f.readline()
        
# list能打开的文件作为参数，把文件内每一行内容作为一个元素
with open(r"haha.txt",'r') as f:
    #以打开的文件f作为参数，创建列表
    l = list(f)
    for line in l:
        print(line)

# read 读取按照字符读取文件内容
#允许输入参数决定读取几个字符，如果没有制定，从当前位置读取到结尾
#否则，从当前位置读取制定个数字符
with open(r"haha.txt", 'r') as f:
    strchar = f.read(12)
    print(len(strchar))
    print(strchar)
    
with open(r"haha.txt", 'r') as f:
    strchar = f.read(1)
    print(len(strchar))
    
    print(strchar)
    
'''
seek(offset,from)
    -移动文件的读取位置（读取指针）
    -from的取值范围
        -0；从文件头开始偏移
        -1：从文件当前位置开始偏移
        -2：从文件末尾开始偏移
    -移动的单位为字节（byte）
    -一个汉字由若干个字节构成
offer偏移量
from从哪儿开始偏移
返回文件指针的当前位置
'''
import time
#打开文件指正在开头 0 处
with open(r"haha.txt", 'r') as f:
    f.seek(100,0)
    strchar = f.read()
    print(strchar)

with open(r"haha.txt",'r') as f:      
    strchar = f.read(3)
    while strchar:
        print(strchar)
        time.sleep(1)
        print(f.read(3))
#作业      