from selenium import webdriver
import unittest 
from time import sleep
from sl_test.ECSHOP import admin_login
from sl_test.ECSHOP.admin_login import test_adminlogin
from sl_test.ECSHOP.admin_login import test_adminlogin
from random import choice
from sl_test.ECSHOP.charge import test_charge
from wlj_test.logining import logining
from selenium.webdriver.remote.utils import handle_find_element_exception
class Ecshop(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://172.31.25.125"
        self.admin_url = "http://172.31.25.125/admin"
    
    def testplace_orders(self):
        driver = self.driver
        logining(driver,'http://172.31.25.125/','AE86','123456')
        ht='window.open("http://172.31.25.125/admin")'
        driver.execute_script(ht)
        handles = driver.window_handles 
        driver.switch_to_window(handles[1])
        test_adminlogin(driver, "admin", "zxc123456789")
        sleep(2)
        handles = driver.window_handles 
        driver.switch_to_window(handles[0])
        
        #首页随机点击某商品
        s=driver.find_elements_by_class_name('goodsItem')
        bg=choice(s)
        b=bg.find_element_by_tag_name('a').get_attribute('href')[34:]
        print(b)
        driver.find_element_by_xpath("//a[@href='goods.php?id="+b+"']").click()
        #点击加入购物车
        driver.find_element_by_xpath("//img[@src='themes/default/images/bnt_cat.gif']").click()
        #点击结算中心
        driver.find_element_by_xpath("//img[@src='themes/default/images/checkout.gif']").click()
        #判定余额是否够订单支付
        l=driver.find_elements_by_tag_name('tbody')
        x=l[-1].find_elements_by_class_name('f4_b')
        actual_value=(x[-1].text)[1:-1]
        y=l[-2].find_elements_by_tag_name('td')
        rest_money=(y[1].text)[2:]
        print(actual_value,rest_money)
        if(float(actual_value)>float(rest_money)):
            handles = driver.window_handles 
            driver.switch_to_window(handles[1])
            sleep(3)
            test_charge(driver, 'AE86',actual_value)
        #点击配送方式
        list1=driver.find_elements_by_xpath("//input[@onclick='selectShipping(this)']")
        choice(list1).click()
        #点击提交订单
        driver.switch_to_window(handles[0])
        driver.find_element_by_xpath("//input[@src='themes/default/images/bnt_subOrder.gif']").click()
        sleep(1)
        order_number=driver.find_element_by_xpath("//font[@style='color:red']").text
        list2=driver.find_elements_by_tag_name('strong')
        order_cost=list2[-2].text
        print(order_number,order_cost)
        self.admin_check(order_number,order_cost)       
    def admin_check(self,order_number,order_cost):
        driver = self.driver
        handles = driver.window_handles 
        driver.switch_to_window(handles[1])
        sleep(1)
        driver.switch_to_frame("menu-frame")  
        driver.find_element_by_link_text("订单列表").click()
        driver.switch_to_default_content()
        driver.switch_to_frame("main-frame")   
        number_actl=driver.find_element_by_xpath("//a[@id='order_0']").text
        print(driver.find_element_by_xpath("//td[@align='right']").text)
        cost_actl=driver.find_element_by_xpath("//td[@align='right']").text
        self.assertEqual(order_number,number_actl)
        self.assertEqual(order_cost,cost_actl)
if __name__ =='__main__':
    unittest.main()
        