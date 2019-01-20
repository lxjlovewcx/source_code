'''
Created on 2018年8月17日

@author: lixue
'''
from _collections import defaultdict
'''
defaultdict
    -当直接读取dict不存在的属性时，直接返回默认值
'''

d1 = {}
from collections import defaultdict
func = lambda: "李雪健"
d2 = defaultdict(func)
d2['one'] =1
d2['two'] =2
print(d2['one'])#有这个属性，返回属性值1
print(d2['four'])#无这个属性，返回默认值  调用上面的函数；李雪健


