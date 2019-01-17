import matplotlib.pyplot as plt #首先导入pyplot 模块  ，并重命名plt，以免重复使用
xvalue = [1, 2, 3, 4, 5]
ysquares = [1, 4, 9, 16, 25]
plt.plot(xvalue, ysquares, linewidth=5) #设置线宽

#设置图表标题， 并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)   #设置title格式
plt.xlabel("value", fontsize=14) #设置x坐标的样式
plt.ylabel("Square of value", fontsize=14)   #设置y坐标的样式

#设置刻度标记的大小
# ax.tick_params(direction='out', length=6, width=2, colors='r',
#  grid_color='r', grid_alpha=0.5)
plt.tick_params(grid_color='r', axis='both', labelsize=14, direction='inout', which='both', )
plt.show() #打开matplotlib查看器，显示绘制的图形

help(plt.tick_params)