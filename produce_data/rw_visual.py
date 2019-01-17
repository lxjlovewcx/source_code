from randon_walk import Random_walk
import matplotlib.pyplot as plt

while True:
    #实例化随机漫步
    random_walk = Random_walk(10000)

    #获取随机漫步点
    random_walk.fill_walk()

    #设置绘图窗口的大小
    plt.figure(dpi= 128, figsize=(10, 6))

    #绘制随机漫步，并体现漫步的先后顺序
    random_walk.y = list(range(random_walk.rw_number))
    plt.scatter(random_walk.x_value, random_walk.y_value, s=8, c=random_walk.y, cmap=plt.cm.Blues, edgecolors='none')  # s为点的大小，c为颜色，x,y为队列的样子

    #突出漫步的起点和终点
    plt.scatter(random_walk.x_value[0], random_walk.y_value[0], s=30, c='red')
    plt.scatter(random_walk.x_value[-1], random_walk.y_value[-1], s=30, c='yellow')

    #隐藏x和y坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    #显示以上信息
    plt.show()

    decision = input("请问继续下一次漫步吗？ y/n")
    if decision == 'n':
        break