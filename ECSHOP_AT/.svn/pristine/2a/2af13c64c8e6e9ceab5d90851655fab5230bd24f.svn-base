# -*- utf-8 -*-



from selenium import webdriver
import unittest 

  
  
  
class test(unittest.TestCase):
    def setUp(self):
        #浏览器选择
        self.driver=webdriver.Chrome()
        #地址
        self.base_url="http://172.31.25.125/"
        #设置元素识别超时时间
        self.driver.implicitly_wait(20)
        #设置页面加载超时时间
        self.driver.set_page_load_timeout(20)
        #设置异步脚本加载超时时间
        self.driver.set_script_timeout(20)
        #浏览器最大化
        self.driver.maximize_window()        
        
    def test(self):
        #打开网站
        driver=self.driver
        driver.get(self.base_url)
        #设置登录信息
        username="刑天"
        password="123456"
        driver.find_element_by_name("submit").click()
        
    
    
    
    
    
    def tearDown(self):
        self.driver.quit()