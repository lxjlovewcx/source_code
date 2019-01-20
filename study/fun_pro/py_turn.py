'''
Created on 2018年8月17日

@author: lixue
'''
'''
返回函数
    -函数可以返回具体的值
    -也可以返回一个函数作为结果
'''
def myf(a):
    print('in myf')
    return None
a = myf(8)
print(a)

def myf2():
    def myf3():
        print("in myf3")
        return 3
    return myf3  #返回了一个函数

print(myf2()())
