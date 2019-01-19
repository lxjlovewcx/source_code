import unittest
from selenium import webdriver
from time import sleep
from TestShop import login_ecshop, login
from TestShop2 import shopping
from TestShop2.shopping import shopping_ecshop
class shopping(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://172.31.25.125/index.php"
        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(20)
       
        

    def testshopping(self):
        driver =self.driver
        driver.get(self.base_url)
        name='圣堂刺客'
        pd='ws12345678'
        login_ecshop(driver,name,pd)
        a = driver.find_element_by_class_name('f4_b')
        self.assertEqual('圣堂刺客',a.text)
        shopping_ecshop(driver)
        #点击结算中心
        driver.find_element_by_xpath('//img[@src="themes/default/imageseckout.gif"]').click()
        #选择配送方式
        driver.find_element_by_xpath('//input[@name="shipping" and @value="1"]').click()
        #选择支付方式
        driver.find_element_by_xpath('//input[@type="radio" and @value="1"]').click()
        #点击提交订单
        driver.find_element_by_xpath('//input[@type="image" and @src="themes/default/images/bnt_subOrder.gif"]').click()
        #查看我的订单
        sleep(1)
        w = driver.find_element_by_xpath('//font[@style="color:red"]').text
        sleep(1)
        #返回用户中心
        driver.find_element_by_link_text('用户中心').click()
        sleep(1)
        #查看我的订单
        driver.find_element_by_link_text('我的订单').click()
        sleep(1)
        q = driver.find_element_by_xpath('//tbody/tr[2]/td[1]').text
        self.assertEqual(w,q)
        print('OK')
        p = driver.find_element_by_xpath('//tbody/tr[2]/td[4]').text
        print(p)
        js = "window.open('http://172.31.25.125/admin')"
        driver.execute_script(js)
        a = driver.window_handles
        driver.switch_to_window(a[1])
        sleep(2)
        driver.find_element_by_name('username').send_keys('圣堂刺客')
        driver.find_element_by_name('password').send_keys('ws12345678')
        driver.find_element_by_class_name('button').click() 
        
    
#        driver.find_element_by_name('username').send_keys()
#        driver.find_element_by_name('password').send_keys()
#        driver.find_element_by_xpath('//input[@type="submit" and value="进入管理中心"]').click()   
    def tearDown(self):
        self.driver.quit()
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()  
