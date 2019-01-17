import matplotlib.pyplot as plt
x_value = list(range(1, 1001))
y_value = list([x**2 for x in x_value])
color = ['red', 'blue', 'yellow', 'black', 'green']

#在此处使用颜色映射，c=y_value, cmap=plt.cm.Blues，将参数c设置为一个y值列表， 并使用参数cmap告诉pyplot使用哪个颜色映射。
# 这些代码将y值较大的映射为深色，y值较小的映射为浅色。
plt.scatter(x_value, y_value, s=50, c=y_value, cmap=plt.cm.Blues, edgecolors='none' )   #s为点的大小，c为颜色，x,y为队列的样子
#设置图表标题， 并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)   #设置title格式
plt.xlabel("value", fontsize=14) #设置x坐标的样式
plt.ylabel("Square of value", fontsize=14)   #设置y坐标的样式

#设置刻度标记的大小
# ax.tick_params(direction='out', length=6, width=2, colors='r',
#  grid_color='r', grid_alpha=0.5)
plt.tick_params(grid_color='r', axis='both', labelsize=14, direction='inout', which='both', )
plt.axis([0, 1100, 0, 1100000])

#plt.show()
#自动保存图片
plt.savefig('square_plot.png', bbox_inches='tight')

help(plt.scatter)