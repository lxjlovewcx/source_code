import unittest
from selenium import webdriver
from time import time
from pageobject.page.index_page import IndexPage
from pageobject.page.register_page import RegisterPage

class TestRegister(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.base_url="http://172.31.31.100:8100/"
        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(20)
        self.driver.set_script_timeout(20)

    def test_01(self):
        driver=self.driver
        driver.get(self.base_url)
        # 定义测试数据
        time_str = str(time()*1000)[:13]
        email=time_str+"@qq.com"
        username=time_str
        password=password1="123456"
        # 点击顶部注册按钮
        IndexPage.click_top_register_link(driver)
        # 实例化一个注册页面的对象
        rp = RegisterPage()
        # 输入必填项
        rp.input_necessary_info(driver, email, username, password, password1)
        # 点击立即注册
        rp.click_register_button(driver)
        # 检查注册结果
        rp.check_register_result(driver)
    
    def test_02(self):
        driver=self.driver
        driver.get(self.base_url)
        # 定义测试数据
        time_str = str(time()*1000)[:13]
        email=""
        username=time_str
        password=password1="123456"
        # 点击顶部注册按钮
        IndexPage.click_top_register_link(driver)
        # 实例化一个注册页面的对象
        rp = RegisterPage()
        # 输入必填项
        rp.input_necessary_info(driver, email, username, password, password1)
        # 点击立即注册
        rp.click_register_button(driver)
        # 检查注册结果
        rp.check_tip(driver, "email")
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()