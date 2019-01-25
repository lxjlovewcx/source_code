import requests
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS #导入作图需要的pygal样式
import pygal #导入pygal用于做柱状图

#   调用api并储存响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
req = requests.get(url)
respon_dict = req.json()
repo_dicts = respon_dict["items"]

names = []
plot_dicts = []
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])
    plot_dict={
        "value": repo_dict["stargazers_count"],
        "lable": repo_dict["description"],
        "xlink": repo_dict["html_url"]
    }
    plot_dicts.append(plot_dict)
    print(plot_dict)

#数据可视化
my_style = LS('#333366', base_style=LCS) #设置基色为深蓝色，并以LCS作为基本样式

my_config = pygal.Config()  #创建config的实例，通过修改config的属性来
my_config.x_label_rotation = 45 #x轴逆时针旋转45度
my_config.show_legend = False  #隐藏图例
my_config.show_minor_y_labels = True
my_config.title_font_size = 24   #设置图表标题的字体大小
my_config.lable_font_size = 14  #副标前
my_config.major_lable_font_size = 18 #主标签
my_config.truncate_label = 15  #截断字符串，可能由于x标签太长，因此采取截断处理
my_config.show_y_guides = False  #不显示y轴的虚线
my_config.width = 1000 #设置宽度，从分利用浏览器页面
my_config.dynamic_print_values = True
my_config.explicit_size = False #给出了图表明确的大小
my_config.height = 600
my_config.include_x_axis =True
my_config.inner_radius = 3
my_config.inverse_y_axis = False #颠倒y轴的数据

bar_chart = pygal.Bar(my_config, style=my_style)  #调用pygal.Bar设置条形图，
bar_chart.title = "Moststars Python Projects on github"
bar_chart.x_labels = names

bar_chart.add('', plot_dicts)
bar_chart.render_to_file(filename="python_pro_stars2.svg")
#help(my_config)
