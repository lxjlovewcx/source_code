import unittest
from selenium import webdriver
from time import sleep,time
from random import choice
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestRegister(unittest.TestCase):

    def setUp(self):
        # 第一步：初始化相关参数
        print("开始进行初始化~~~~~~~~~~~~~")
#         self.driver = webdriver.Firefox()
        self.driver = WebDriver(command_executor='http://172.31.17.82:4444/wd/hub',
                                desired_capabilities=DesiredCapabilities.CHROME)
        self.base_url = "http://172.31.31.100:8200/"
        # 设置元素识别超时时间
        self.driver.implicitly_wait(20)
        # 设置页面加载超时时间
        self.driver.set_page_load_timeout(20)
        # 设置异步脚本加载超时时间
        self.driver.set_script_timeout(20)

    def test_01(self):
        print("开始进行操作~~~~~~~~~~~~~")
        # 第二步：打开被测网站
        driver = self.driver
        driver.get(self.base_url)
        # 第三步：执行测试动作
        # 定义注册时所需的邮箱地址、密码、名字
        email = str(time()*1000)[:13]+"@qq.com"
        password = "123456"
        name_list = ["艾","安","昂","敖","奥","巴","霸","白","柏",
                     "拜","班","包","保","葆","豹","鲍","暴","卑",
                     "贲","毕","闭","秘","边","鞭","彪","别","宾",
                     "邴","秉","薄","卜","布","部","才","蔡","仓",
                     "苍","操","曹","策","岑","柴","镡","昌","苌",
                     "常","昶","畅","唱","晁","巢","朝","车","陈",
                     "谌","成","承","晟","乘","程","池","迟","充",
                     "种","崇","丑","侴","初","储","楚","禇","揣",
                     "啜","春","椿","慈","次","从","丛","爨","崔",
                     "萃","寸","达","笪","王"]
        name = choice(name_list)+choice(name_list)
        # 点击 注册
        driver.find_element_by_link_text("注册").click()
        # 输入邮箱地址 
        driver.find_element_by_name("email").send_keys(email)
        # 输入密码 
        driver.find_element_by_name("passwd").send_keys(password)
        # 输入确认密码 
        driver.find_element_by_name("repasswd").send_keys(password)
        # 输入姓名 
        driver.find_element_by_name("name").send_keys(name)
        # 设置性别为男 
        driver.find_element_by_xpath("//input[@name='sex' and @value='1']").click()
        # 点击选择地区  
        driver.find_element_by_class_name("btn_b").click()
        # 点击 四川
        driver.find_element_by_link_text("四川").click()
        # 点击 成都市
        driver.find_element_by_link_text("成都市").click()
        # 点击确定按钮 
        driver.find_element_by_name("input").click()
        # 设置隐私为任何人可见 方式一：直接找
#         driver.find_element_by_xpath("//select[@name='baseinfoprivacy']/option[@value='0']").click()
        # 方式二：Select类
        element = driver.find_element_by_name("baseinfoprivacy")
        sel = Select(element)
        sel.select_by_value("0")
        # 方式三：一级一级找
#         driver.find_element_by_name("baseinfoprivacy").find_element_by_xpath("//option[@value='0']").click()
        # 点击立即注册  
        driver.find_element_by_class_name("btn_reg").click()
        sleep(2)
        # 点击 基本资料
        driver.find_element_by_link_text("基本资料").click()
        # 定位到姓名的input元素，取出其value属性的值进行对比 
        actual_name = driver.find_element_by_name("name").get_attribute("value")
        # 第四步：判断测试结果
        self.assertEqual(name, actual_name)
        print("完成操作~~~~~~~~~~~~~")
        
    def tearDown(self):
        # 第五步：释放资源
        self.driver.quit()
