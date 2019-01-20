'''
Created on 2018年8月17日

@author: lixue
'''
'''
闭包（closure）
当一个函数在内部定义函数，并且内部的函数应用外部函数的参数或者局部变量，当内部函数被当做返回值时候相关参数和变量保存在返回的函数中，这种结果，叫做闭包。
上面模块py_turn中的myf4是一个标准闭包结构
'''
#闭包常见坑
def count():
    #定义列表，列表中存放的是定义地函数
    fs =[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())

'''
出现的问题：
    -造成上述状况的原因是，返回函数应用了变量i，i并非立即执行，而是等到三个函数都返回时候才统一 使用，此时i已经
        变为3，最终调用的时候，都返回的是3*3
    - 此问题描述 为：返回闭包时，返回函数不能应用任何循环变量
    -解决方案：在创建一个函数，用改函数的参数绑定循环变量的当前值，无论改循环变量以后如何变化，已经绑定的函数参数值不再变化
 '''
 # 修改上述函数
 
def count2():
    #定义列表，列表中存放的是定义地函数
    def f(j):
        return j*j
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3 = count2()
print(f1)
print(f2)
print(f3)

