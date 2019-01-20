'''
Created on 2018年8月17日

@author: lixue
'''

'''
字符串本省就是可以迭代的
'''

from collections import Counter
from builtins import help
help(Counter)
c = Counter("safsdafsdagdsgsdaflksajklfsdjafkszanf")
print(c) #对其中每一个字符或者数字进行统计，键为字符，值为个数
#Counter({'s': 8, 'a': 7, 'f': 6, 'd': 5, 'k': 3, 'g': 2, 'l': 2, 'j': 2, 'z': 1, 'n': 1})
s = ['rwer','fsdfs','rwer'] 
print(Counter(s)) # Counter({'rwer': 2, 'fsdfs': 1})