'''
Created on 2018年8月17日

@author: lixue
'''
'''
过滤函数：对一组数据进行过滤，符合条件的数据会生成一个新的列表返回
跟map比较
    -不同：都对列表的每一个元素注意进行操作
    -不同
        -map会生成一个跟原来数据相对应的新队列
        -filter不一定，只要符合要求的才能进入新的数据集合
    filter函数怎么写：
        -利用给定函数进行判断
        -返回值一定是个布尔值
        -调用格式：filter(f,data),f为过滤函数，data是数据
'''
def iseven(a):
    return a%2 ==0
rst = filter(iseven,[i for i in range(10)])
print(rst)
print(type(rst))
print([i for i in rst])
print(list(rst))

