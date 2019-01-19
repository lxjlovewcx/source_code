import requests
import json
import matplotlib.pyplot as plt
import pygal
import math
from itertools import groupby


json_url = "https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"
request = requests.get(json_url)
with open('hehe.json', 'w') as f:
    f.write(request.text)
with open('hehe.json') as f:
    file_objects = json.load(f)
77
dates = []
months = []
weeks = []
weekdays = []
closes = []

for file_object in file_objects:
    dates.append(file_object['date'])
    months.append(file_object['month'])
    weeks.append(file_object['week'])
    weekdays.append(file_object['weekday'])
    closes.append(int(float(file_object['close'])))

print(closes)

def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for i, j in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in j]
        xy_map.append([i, sum(y_list) / len(y_list)])
    x_value, y_value = [*zip(*xy_map)]
    line_chart = pygal.Line()     #由于设置了x_label_rotation 参数,导致无法显示x数值。
    line_chart.title = title
    line_chart.x_labels = x_value
    line_chart.add(y_legend, y_value)
    line_chart.render_to_file("closes of price1.svg")
    return line_chart

index = dates.index("2017-12-01")
line_chart_month = draw_line(months[:index], closes[:index], title="月均收盘价", y_legend="price")
line_chart_month