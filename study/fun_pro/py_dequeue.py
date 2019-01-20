'''
Created on 2018年8月17日

@author: lixue
'''
'''
队列
dequeue

链表和数组：是很难解决的问题
数组的有点：顺序快
缺点：在插入和删除的时候，数据需要全部进行重排，都是i/o操作，很消耗资源。
链表 ：
python中的list（有序列表），在内存中存在连续的问题，比如涉及到插入、删除的操作

dequeue
    -比较方便的解决了频繁删除插入带来的效率问题
'''
from collections import deque
q = deque(['1','2','3'])
print(q)
q.append('4')
print(q)
q.appendleft('5')
print(q)
