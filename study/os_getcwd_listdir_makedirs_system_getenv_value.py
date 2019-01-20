'''
Created on 2018年8月16日

@author: lixue
'''
#os -操作系统相关 ，主要是文件操作
# -*- coding = utf-8 -*-
import os
print(os.getcwd())#显示当前工作目录的路径

#os 模块
#getcwd() 获取当前的工作目录
#格式：os.getcwd()
#返回值：当前工作目录的字符串
# mydir = 
# print(mydir)
os.chdir('D:\文档\worksapce')#改变当前工作目录
print(os.getcwd())
#listdir() 获取一个目录中所有子目录和文件的名称列表
#格式：os.listdir(路径)
print(os.listdir())#显示当前工作目录下的所有文件

#makedirs() 递归创建文件夹
#格式：os.makedirs(递归路径)
#返回值：无
#递归路径：多个文件夹层层包含的路径就是递归路径 例如：
rst = os.makedirs("dana5")#在当前路径下创建文件夹dana1
# print(rst)#在python中不管有没有返回值，如果没有返回none，如果有返回0
print(os.system("ls"))


#system() 运行系统shell命令
#格式;os.system( 系统命令)
#返回值：打开一个shell或者终端界面
#ls是列出当前文件和文件夹的系统命令
rst =os.system("ls")
print(rst)
os.system("touch haha") #执行系统命令兴建文件
os.system("cat haha") #执行系统命令显示文件内容

#getenv() 获取指定的系统环境变量值
#相应的还有putenv
#格式：os.getenv('环境变量名')

print(os.getenv("PATH"))#$获取当前PATH路径下额环境变量


#exit() 退出当前程序
#格式：exit()
#返回值：无

'''
值部分
os.curdir:current dir,当前目录
os.pardir:parent dir,父目录
os.sep:当前系统的路径分隔符
    -windows:"\"
    -linux:"/"  
os.linesep:当前系统的换行符号
    -windows:"\r\n"
    -linux,unix,macos:"\n"
os.name:当前系统名称
    -windows:nt
    -mac,unix,linux:posix
使用上述符号，使程序具有可移植性
'''
print(os.name)

