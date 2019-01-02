#打印矩形
for i in range(0,5):
    for j in range(0,6):
        print("*",end=" ")
    print()
print("="*20)
#help(print)
'''
打印空心的矩形,自己的想法是分两个分支，第一行和最后一行为一个分支，中间的为一个分支。中间分支
的时候又要继续分支两种情况。出现下面问题的原因是* 和空格所占的大小不一样。是自己的问题

'''
for i in range(0,5):
    if i ==0 or i ==4:
        for j in range(0,6):
            print("*",end=" ")
        print()
    else:
        for j in range(0,6):
            if j==0 or j==5:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

'''
这个是正确的解法，要正确理解循环的含义。从整体上来考虑。i为控制行数，j为控制列数。
'''
for i in range(0,5):
    for j in range(0,6):
        if i == 0 or i == 4 or j == 0 or j == 5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
打印直角三角形,打印各种类型的三角形，使用的是数学中的方法，线性方程。同时以上的空心矩形也是使用线性方程的思想。
'''
for i in range(5):
    for j in range(5):
        if i >= j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(5):
    for j in range(5):
        if i <= j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(5):
    for j in range(5):
        if i+j >= 4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("* "*20)
#help(range)

a = range(1,3)
print(a)
#print(a.count(1))
print(a.index(2))

#help(list)
a = []
b = list(range(3))
a.extend(b)
print(a)

"""
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object   此处返回一个range对象
 |  range(start, stop[, step]) -> range object  此处返回一个range对象
 |  
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
 |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).
 
 返回一个包含开始，不包含结束的整型序列的对象，这些确切地讲其实是一个具有四个元素列表的有效切片。
 | 
方法定义如下： 
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __reduce__(...)
 |      helper for pickle
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      Return a reverse iterator.
 |  
 range(3).count(1) 表示返回1在生成的列表中的个数。
 |  count(...)
 |      rangeobject.count(value) -> integer -- return number of occurrences of value
 | 
range(1,3).index(2) 
 |  index(...)
 |      rangeobject.index(value, [start, [stop]]) -> integer -- return index of value.
 |      Raise ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 数据描述定义在此：
 |  Data descriptors defined here:
 |  
 |  start
 |  
 |  step
 |  
 |  stop
 
 """

"""
Help on class list in module builtins:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.n
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      L.__reversed__() -- return a reverse iterator over the list
 |  
 |  __rmul__(self, value, /)
 |      Return self*value.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      L.__sizeof__() -- size of L in memory, in bytes
 |  
 |  append(...)            在列表最后添加一个元素，这个在外星人入侵中制造子弹时使用过
 |      L.append(object) -> None -- append object to end
 |  
 |  clear(...)            清空整个列表
 |      L.clear() -> None -- remove all items from L
 |  
 |  copy(...)               列表的浅复制
 |      L.copy() -> list -- a shallow copy of L
 |  
 |  count(...)           这个和range也重复了
 |      L.count(value) -> integer -- return number of occurrences of value
 |  
 |  extend(...)          扩展列表，在列表后面添加一个可迭代的对象。自身的返回值为空，但是对应l列表的确扩展了。
 |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
 |  
 |  index(...)         这个和range重复了
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  insert(...)               在指定的下标前插入对象
 |      L.insert(index, object) -- insert object before index
 |  
 |  pop(...)          删除最后一个元素，并返回这个元素。也可以删除指定地址的元素并返回这个元素。
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(...)      移除列表中指定的值
 |      L.remove(value) -> None -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(...)           将列表中的元素反转
 |      L.reverse() -- reverse *IN PLACE*
 |  
 |  sort(...)          将列表中的元素排序
 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None
 """





