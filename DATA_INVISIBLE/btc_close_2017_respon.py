import requests
import json
import matplotlib.pyplot as plt
import pygal
import math
from itertools import groupby
json_url = "https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"
request = requests.get(json_url)  #<Response [200]>
#print(request.text)  #其中包含了很多的 换行符，不利于python处理
file_url = request.json()  #一个list列表 ，将其转换为标砖的python list格式
#print(file_url)

with open('haha.json', 'w') as f:
    f.write(request.text)    #此处需要传入一个字符串格式的对象

file_name = "haha.json"
with open(file_name) as f: #json.loads()读取的是字符串，二进制，不能是TextIOWrapper
    #print(f) #<_io.TextIOWrapper name='haha.json' mode='r' encoding='cp936'>
    file_objects = json.load(f)

dates = []
months = []
weeks = []
weekdays = []
closes = []

#打印每一天的信息
for file_object in file_objects:
    dates.append(file_object['date'])
    months.append(file_object['month'])
    weeks.append(file_object['week'])
    weekdays.append(file_object['weekday'])
    closes.append(math.log10(int(float(file_object['close']))))
 #   print("{} is week {} month {} {}, close price is {} RMB".format(date, month, week, weekday, close))
'''
plt.plot(dates, closes, linewidth=2)
plt.title("gupiao price of 2017", fontsize=25)
plt.xlabel("日期", fontsize=5)
plt.ylabel("price", fontsize=5)
plt.show()
'''

#line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False) #让x轴上的日期标签顺时针旋转20
#line_chart.title = '收盘价(¥)'
#line_chart.x_labels = dates
#N = 20
#line_chart.x_labels_major = dates[::N] #设置x轴标签属性，每隔20个显示一次。
#line_chart.add('收盘价', closes)
#line_chart.render_to_file("closes of price1.svg")


def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    '''
    for i, j in groupby(sorted(z), key=lambda _: _[0]):
        print(i, j)
        for k in j:
            print(k)
    执行结果为
    1 <itertools._grouper object at 0x03711430>
    (1, 11)
    (1, 22)
    2 <itertools._grouper object at 0x037117D0>
    (2, 33)
    (2, 44)
    3 <itertools._grouper object at 0x037119B0>
    (3, 55)
    4 <itertools._grouper object at 0x037117D0>
    (4, 66)
    5 <itertools._grouper object at 0x037119B0>
    (5, 23)
    (5, 24)
    '''
    for i, j in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]): #sorted返回一个新的list列表，按照key从小到大的顺序。
        y_list = [v for _, v in j]
        xy_map.append([i, sum(y_list)/len(y_list)])
                                                                        #*zip()函数是zip()函数的逆过程，将zip对象变成原先组合前的数据。
    x_value, y_value = [*zip(*xy_map)]                                    #此处的语法很容易错，不要忘记[]括号。
    line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
    line_chart.title = title
    line_chart.x_labels = x_value
    line_chart.add(y_legend, y_value)
    line_chart.render_to_file("closes of price1.svg")
    return line_chart
index = dates.index("2017-12-01")
line_chart_month = draw_line(months[ :index], closes[ :index], title="月均收盘价", y_legend="price")
#N = 20
#line_chart.x_labels_major = dates[::N] #设置x轴标签属性，每隔20个显示一次。
line_chart_month
