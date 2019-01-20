'''
装饰器（decrator）
    -在不改动函数代码的基础上无限制扩展函数功能的一种机制，本质上讲，装饰器是一个返回函数的高阶函数
    -装饰器的使用：使用@语法，即在每次要扩展的函数定义前使用@+函数名
任务：
对hello函数进行功能扩展，每次执行hello前打印当前系统时间
'''
import time
from tornado.test.httpclient_test import HelloWorldHandler
#高阶函数，以函数作为参数
def printtime(f):
    def wrapper(*args,**kwargs):
        print("time:",time.ctime()) #装饰器在工作的过程中，先执行这一行代码，再执行下面
        return f(*args,**kwargs)#返回函数的内容，而后面返回函数就是修饰的函数
    return wrapper

@printtime
def hello():
    print("hello HelloWorldHandler")
hello()

'''
上面就是讲高阶函数和返回函数合并到一块了而已
上面定义了装饰器，使用的时候需要使用@，此符号是python的语法糖
@printtime  装饰后面的函数
def hello():
    print("hello world)
hello()

装饰器的好处，一旦定义，则可以装饰任意函数
一旦被其装饰，则把装饰器的功能直接添加到定义的函数的功能之上
'''
@printtime
def hello2():
    print("wohen kaixing ")
hello2()

'''
上面对函数的装饰使用了系统定义的语法糖
下面开始手动执行下装饰器
先定义函数
'''
hello3 = printtime(hello2)#装饰器中传入被修饰函数，返回一个包含传入函数的一个新的函数
hello3()
printtime(hello2)() 
