import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = "death_valley_2014.csv"  #文件名
with open(filename) as f:      #使用open方法获取文件对象并将其存储在f中， with方法不用使用close语句。
    reader = csv.reader(f)
    #将f文件对象传递给csv.reader（），返回reader对象
    header_row = next(reader)  #csv中存在next()函数，返回文件中的下一行，获取第一行文件头
    #并将每项值作为一个元素储存在列表中，
    enumerate = enumerate(header_row)  #返回一个enmerate 对象
    print(list(enumerate))     #使用list可以将可迭代对象转换为列表
    for index, value in enumerate:
        print(index, value)
date = []
temperature = []
low_temperature = []
with open(filename) as f:      #使用open方法获取文件对象并将其存储在f中， with方法不用使用close语句。
    reader = csv.reader(f)
    header_row = next(reader) #读取第一行
    for reader_line in reader:  #遍历将从第二行开始
        try:
            reader_date = datetime.strptime(reader_line[0],"%Y-%m-%d")
            reader_tem = int(reader_line[1])
            reader_lowtem = int(reader_line[2])
        except ValueError:
            print(reader_line[0] + "数据不正常")
        else:
            date.append(reader_date)
            temperature.append(reader_tem)
            low_temperature.append(reader_lowtem)

#根据数字绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(date, temperature, c ='red', linewidth=1)
plt.plot(date, low_temperature, c ='blue', linewidth=1)
plt.fill_between(date, temperature, low_temperature, facecolor='blue', alpha=0.5)
#设置图形格式
plt.title("Daily high temperature, 2014", fontsize=24)
plt.xlabel(" ", fontsize=14)
plt.ylabel("temperature(f)", fontsize=14)
plt.tick_params(axis='both', labelsize=12, direction='inout', which='both', )
fig.autofmt_xdate()
plt.show()



