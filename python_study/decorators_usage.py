"""
常见装饰器模式如下：
1：参数检查
2：缓存
3：代理
4：上下文提供者
"""

# 1 参数检查
rpc_info = {}

def xmlrpc(in_=(), out=(type(None),)):
    def _xmlrpc(function):
        #注册签名
        func_name = function.__name__
        rpc_info[func_name] = (in_, out)
        def _check_types(elements, types):
            """
            用来检查类型的子函数
            :param elements:
            :param types:
            :return:
            """
            if len(elements) != len(types):
                raise TypeError('argument count is wrong')
            typed = enumerate(zip(elements, types))
            for index, couple in typed:
                arg, of_the_right_type = couple
                if isinstance(arg, of_the_right_type):
                    continue
                raise TypeError(
                    'arg #%d should be %s' % (index,
                            of_the_right_type))
            #包装过的函数
        def __xmlrpc(*args):
            checkable_args = args[1:]
            _check_types(checkable_args, in_)
            res = function(*args)
            if not type(res) in (tuple, list):
                checkable_res = (res,)
            else:
                checkable_res = res
            _check_types(checkable_res, out)

            return res
        return __xmlrpc
    return _xmlrpc

class RPCView:
    @xmlrpc((int, int))
    def meth1(self, int1, int2):
        print('received %d and %d' % (int1, int2))

    @xmlrpc((str,), (int,))
    def meth2(self, phrase):
        print('received %s' % phrase)
        return 12

rpc_info
my = RPCView()
my.meth1(1, 2)
#my.meth2(2)

# 2 缓存
# 4 上下文提供者
from threading import RLock
lock = RLock()

def synchronized(function):
    def _synchronized(*args, **kwargs):
        lock.acquire()
        try:
            return function(*args, **kwargs)
        finally:
            lock.release()
    return _synchronized

@synchronized
def thread_safe():
    print("no prablem")

thread_safe()