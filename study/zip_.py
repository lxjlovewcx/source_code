'''
Created on 2018年8月16日

@author: lixue
'''
'''
zip- 压缩包
模块名称叫zipfile
zipfile.zipfile(file[,mode[,compression[,allowzip64]]])
创建一个zipfile对象，表示一个zip文件。参数file表示文件的路径或类对象文件（）
'''

import zipfile
zf = zipfile.ZipFile("tuling.zip")#创建此压缩文件的实例
zf.getinfo("名称")#获取名称文件的信息
zf.namelist()#获取压缩文档中所有文件的名称列表
zf.extractall("path")