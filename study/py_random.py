'''
Created on 2018年8月16日

@author: lixue
'''
import random
'''
随机数
random
所有的随机模块都是伪随机
'''
print(random.random())#0到1之间的小数,0.21089420008941084
print(random.randint(0,100))#随机生成0,100之间包含0,100之间的整数

#choice()
l = [str(i)+"haha" for i in range(10)]
print(l)
rst = random.choice(l)#随机从列表中选择一个值
print(rst)#['0haha', '1haha', '2haha', '3haha', '4haha', '5haha', '6haha', '7haha', '8haha', '9haha'],4haha

l1= [i for i in range(10)]
print(l1)
l2 = random.shuffle(l1)
print(l2)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]None

help(random.shuffle)

l1= [i for i in range(10)]
print(l1)
random.shuffle(l1)
print(l1)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],[3, 5, 8, 4, 7, 1, 9, 2, 0, 6]