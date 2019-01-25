from functools import wraps
class WithoutDecorators():
    """
    此为不适用装饰器语法将方法定义为类方法和静态方法
    """
    def some_static_method():  #因为此处将其处理为静态方法，因此不需要传入self
        print("this is static method")
    some_static_method = staticmethod(some_static_method) #此为装饰器的显示写法
    def some_class_method(cls):  #cls 表示类本身
        print("this is class method")
    some_class_method = classmethod(some_class_method)

WithoutDecorators.some_static_method() # 结果为this is static method
WithoutDecorators.some_class_method()  # 果为this is class method

hello = WithoutDecorators()
hello.some_class_method()  # 结果为this is class method
hello.some_static_method() # 结果为this is static method
hello.some_static_method() # 结果为this is static method

class WithDecorators:
    """
    此处是使用修饰器将下面两个方法转化为类方法和静态方法，代码更加
    简短和易于理解。
    此为装饰器的隐身式写法
    """
    @staticmethod  #定义静态方法的好处是不需要实例化，直接用类调用即可。
    def some_static_method():
        print("this is static method")

    @classmethod  # 定义类方法时第一个参数总是cls。而且必须是
    def some_class_method(cls):
        print("this is class method")

# @some_decorator
    # 装饰器的一般写法
def decorated_function():
    pass

    """
    将以上转化为装饰器的显示写法
    """
def decorated_function():
    pass
#decorated_function = some_decorator(decorated_function)

#装饰器函数的实现的可能
# 1 作为一个函数

def mydecorator(function):
    def wrapped(*args, **kwargs):
        print("程序开始") #在调用原函数之前，做些什么
        result = function(*args, **kwargs)
        print("程序结束")# 调用结束后，做些什么
        return result #返回原函数
    return wrapped #返回装饰函数

@ mydecorator
def my():
    print("i love you, wangchengxi")

my()
mydecorator(my)() #my 已经被装饰了，所以如此执行的化结果如下，开始和结束被执行两次
# 程序开始
# 程序开始
# i love you, wangchengxi
# 程序结束
# 程序结束

# 2 作为一个类
class DecoratorAsClass:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print("程序开始") #在调用原函数之前，做些什么
        result = self.function(*args, **kwargs)
        print("程序结束")# 调用结束后，做些什么
        return result  # 返回原函数

@ DecoratorAsClass
def my():
    print("i love you, wangchengxi")

my()
DecoratorAsClass(my)()

# 3 参数化装饰器
def repeat(number=3):
    def actual_decorator(function):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(number):
                result = function(*args, **kwargs)
            return result
        return wrapper
    return actual_decorator

@repeat() #此处必须加括号，带参数，不然会报错，提示actual_decorator函数
          # 缺少位置参数function
          #实际上这个修饰函数需要两个参数，如果没有括号，会认为将foo作为第一个参数传给
#repeat，而actual_decorator函数则会缺少位置参数function
def foo():
    print("foo")

foo()
# 4 保存内省的装饰器

def dummy_decorator(function):
    def wrapped(*args, **kwargs):
        """包装函数内部文档"""
        return function(*args, **kwargs)
    return wrapped

@dummy_decorator
def function_with_important_docstring():
    """这是我们想要保存的重要文档字符串"""
#function_with_important_docstring.__name__ # 'wrapped'
#function_with_important_docstring.__doc__  # '包装函数内部文档'


# 一下为经过改良后的代码，
#需要导入from functools import wraps
# 在被返回的函数前面添加@wraps(function) 被修饰函数
def new_dummy_decorator(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        """包装函数内部文档"""
        return function(*args, **kwargs)
    return wrapped

@new_dummy_decorator
def function_with_important_docstring():
    """这是我们想要保存的重要文档字符串"""

#function_with_important_docstring.__name__ # ''function_with_important_docstring''
#function_with_important_docstring.__doc__  # '这是我们想要保存的重要文档字符串'