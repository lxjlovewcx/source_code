'''
Created on 2018年8月16日

@author: lixue
'''
import shutil
'''
copy()复制文件
格式：shutil.copy(来源路径，目标路径)
返回值：返回目标路径
拷贝的同时，可以给文件重命名
'''
# shutil.copy(src, dst)
# shutil.copy2(src, dst)
# shutil.c
'''
copy2()复制文件，保留元数据（文件信息）
格式：shutil.copy2(来源路径，目标路径)
返回值:返回目标路径
注意：copy和copy2的唯一区别在于copy2复制文件时尽量保留元数据
'''

'''
copyfile()将一个文件中的内容复制到另外一个文件当中
shutil.copyfile('源路径'，'目标路径')
返回值：无
'''

# shutil.copyfile("src", "dst")


'''
move()移动文件/文件夹
格式：shutil.move(源路径，目标路径)
返回值：目标路径！
rst = shutil.move()
'''

'''
归档和压缩
归档：把多个文件或者文件夹合并到一个文件当中
压缩：用算法把多个文件或则文件夹无损或者有损合并到一个文件当中
是想得到一个叫做lixuejian.haha的归档文件
make_archive()归档操作
格式：shutil.make_archive('归档后的目录和文件名','zip','需要归档的文件夹')"zip", "tar", "gztar","bztar", or "xztar".
'''

help(shutil.make_archive)

'''
解包命令 shutil。unpack_archive('归档文件地址'，'解包字后的地址')
返回值：解包之后的地址
'''

