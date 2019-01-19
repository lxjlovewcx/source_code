from die import  Die
import pygal  #导入python可视化包，生成可以缩放的矢量文件, pygal使图具有交互性，如果将鼠标放到任何一张图片
# 上面，都会显示相关的信息。

die1 = Die()
die2 = Die(10)
results = []

#获得摇塞子的结果
for i in range(1000):
    roll_point = die1.roll() + die2.roll()
    results.append(roll_point)

#获取指定的点数
points = list(range(1+1, die1.side_numbers + die2.side_numbers +1))

#获取数据的挖掘结果
roll_result = []
for i in points:
    point_result = results.count(i)
    roll_result.append(point_result)

#对结果进行可视化
hist = pygal.Bar() #创建一个pygal条形图的实例
hist.title = "result of rolling D10 and D6 1000 times"
hist.x_labels = points
hist.x_title = " RESULT"
hist.y_title = "frequency of result"

hist.add('D10 D6', roll_result)
hist.render_to_file('die_visual7.svg')
help(pygal.Bar)


