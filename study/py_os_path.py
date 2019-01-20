'''
Created on 2018年8月16日

@author: lixue
'''
'''
#abspath()将路径转化为绝对路径
#absolute 绝对
# 格式：os.path.abspath(' 路径')
#返回值：路径的绝对路劲格式
#linux中
#。点号，代表当前目录
。。双点，代表父目录
'''
import os.path as pa
pas = pa.abspath(".")
print(pas)

'''
basename() 获取路径中的文件名部分
格式：os.path.basename(路径)
返回值：文件名字符串
'''
bn = pa.basename("D:\文档\worksapce\study")
print(bn)
bn = pa.basename("D:\文档\worksapce")
print(bn)
'''
join()将多个路径拼合成一个路径
格式：os.path.join(路径1，路径2.。。)
返回值：组合之后的新路径字符串
'''
bd = "worksapce\study"
bs = "D:\文档\worksapce"
print(pa.join(bs,bd)) #D:\文档\worksapce\worksapce\study

'''
split()将路径切割为文件夹部分和当前文件部分
#格式：os.path.split(路径)
#返回值：路径和文件名组成的元祖
'''
t = pa.split("D:\文档\worksapce\study")
print(t)
d,p = pa.split("D:\文档\worksapce\study") 
print(d,p)
'''
isdir()检测是否为目录
格式：os.path.isdir(路径)
返回值：布尔值
'''
rst = pa.isdir("D:\文档\worksapce\study")
print(rst)

'''
exists()检测文件或者目录是否存在
os.path.exists(路径)
返回值：布尔值
'''

e = pa.exists("D:\文档\worksapce\study")
print(e)
