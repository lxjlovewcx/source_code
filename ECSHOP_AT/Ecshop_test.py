import unittest,os
from selenium import webdriver
import sys
from lxj_test.code.HTMLTestRunner import HTMLTestRunner
from lxj_test.code.zuce_test import zuce_test
from lxj_test.code.denglu_test import denglu_test
from jn_test.addgoods import goods
from _datetime import datetime
from wyl_test.pl import test
from wlj_test import place_order 
from sl_test import ECSHOP_MAIN
class Ecshop_test(unittest.TestCase):  
    username = ""
    pwd = ""
    email = ""
    answerdata = ""
    phonenumber = ""
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url1 = "http://172.31.25.125/"
        self.base_url2 = "http://172.31.25.125/admin/"

        #识别元素地超时时间
        self.driver.implicitly_wait(10)
        #页面加载地超时时间
        self.driver.set_page_load_timeout(10)
        #设置脚本地加载时间
        self.driver.set_script_timeout(10)
    def test_lixuejian(self):
        driver = self.driver
        base_url1 = self.base_url1
        driver.get(base_url1)
        Ecshop_test.username,Ecshop_test.pwd,Ecshop_test.email,Ecshop_test.answerdata,Ecshop_test.phonenumber = zuce_test(driver)
    def test_lixuejian2(self):
        base_url1 = self.base_url1
        driver = self.driver
        driver.get(base_url1)
        denglu_test(driver, Ecshop_test.username, Ecshop_test.pwd, Ecshop_test.email,Ecshop_test.answerdata)
    def tearDown(self):
        self.driver.quit()        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Ecshop_test("test_lixuejian"))
    suite.addTest(Ecshop_test("test_lixuejian2"))
    suite.addTest(place_order.Ecshop("testplace_orders"))
    suite.addTest(goods("test_goods")) 
    suite.addTest(test("test")) 
    suite.addTest(ECSHOP_MAIN.ECHOP_MAIN("test_main"))       
    cur_dir = os.getcwd()#获取当前路径
    sys.path.append(cur_dir)
    dt = datetime.now()
    now = dt.strftime("%Y-%m-%d_%H_%M_%S")
#     now = str(time())
    report_folder = cur_dir + os.sep +'report' + os.sep
    filename = report_folder + now + '_result.html'  # 测试报告的路径名
    print(filename)
    fp = open(filename,'wb')  #以二进制的格式，以写的方式，打开报告文件
    runner = HTMLTestRunner(
        stream=fp,
        title='接口自动化测试报告',
        description='用例执行情况：',
        )
    #runner = unittest.TextTestRunner()  
    runner.run(suite)
#     

        
        
        
        
        