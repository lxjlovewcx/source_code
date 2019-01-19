import unittest,os
from selenium import webdriver
from random import choice
from selenium.webdriver.support.select import Select
import sys
from test.test_html import HtmlTests
from lxj_test.HTMLTestRunner import HTMLTestRunner
from asyncio.tasks import sleep
from datetime import *
from time import time,sleep
from lxj_test.code import zuce_test, backlogin, backcheckuser, goodclass,\
    goodbrand, addnewgood, checknewgood, buygoods
from lxj_test.code import exchangewindows
from lxj_test.code import denglu_test
class Ecshop_test(unittest.TestCase):
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
    def test_zuce(self):
        driver = self.driver
        base_url1 = self.base_url1
#         base_url2 = self.base_url2
        driver.get(base_url1)
        #注册用户并返回用户名、密码、电子邮箱、安全回答问题、电话号码信息
        username,pwd,email,answerdata,phonenumber = zuce_test.zuce_test(driver)
        driver.get(base_url1)
        #使用注册返回地信息登陆用户 
        denglu_test.denglu_test(driver,username,pwd,email,answerdata)
        #使用js代码打开新的窗口
        js="window.open('http://172.31.25.125/admin')"
        driver.execute_script(js)
        sleep(1)
        backusername = "lxj"
        backpassword = "lxj123456"
#         list_handles = []
#         list_handles = driver.window_handles()
#         print(driver.window_handles())
        #切换到新地窗口
        exchangewindows.exchangewindows(driver)
        #后台登陆,进入到后台默认页面
        backlogin.backlogin(driver, backusername, backpassword)
        #检查后台用户，由默认页面进入，由默认页面退出
        backcheckuser.backcheckuser(driver, username, email, phonenumber)
        #添加新商品分类，由默认页面进入，由默认页面退出,返回商品分类值
        goodclass = goodclass.goodclass(driver)
        #添加新商品品牌，由默认页面进入，默认页面退出，返回商品品牌
        goodbrand = goodbrand.goodbrand(driver)
        #添加具有goodclass和goodbrand地新商品，有默认页面进入，返回新商品名称
        newgood = addnewgood.addnewgood(driver, goodclass, goodbrand)
        sleep(2)
        #退出默认页面
        driver.switch_to_default_content()
        #检查新商品，通过newgood,goodclass,goodbrand检查商品
        checknewgood.checknewgood(driver, newgood, goodclass, goodbrand)
        #检查完成商品后，切换到前台购买商品
        exchangewindows.exchangewindows(driver)
#         username = '李雪健'
#         email = '851677798@qq.com'
#         phonenumber = '12345678901'
#         fstate2,fstate3,fstate4,fstate5,fstate6,fstate7 = ","","","","退货,未付款,未发货","已确认,未付款,未发货"
#         bstate2,bstate3,bstate4,bstate5,bstate6 = ","","","已发货","退货,未付款,未发货","已确认,未付款,未发货"
        provice = "四川"
        city = '成都'
        area = '锦江区'
        #前台购买商品,返回订单号
        goodorder = buygoods.buygoods(driver, goodclass, provice, city, area, username, email, phonenumber)
        #前台状态一：
        fstate1 = "已确认,已付款,未发货"
        self.frontgoodstate(fstate1)
        sleep(1)
        #切换到后台
        exchangewindows.exchangewindows(driver)
        driver.switch_to_default_content()
        #查询订单
        self.searchorder(goodorder)
        #后台订单状态一
        bstate1 = "已确认,已付款,未发货"
        self.backgoodstate(bstate1)
        sleep(1)
        #执行配货操作
        driver.find_element_by_name("prepare").click()
        #切换窗口到前台
        exchangewindows.exchangewindows(driver)
        sleep(1)
        #查看前台状态2
        fstate2 = "已确认,已付款,配货中"
        self.frontgoodstate(fstate2)
        sleep(1)
        #切换窗口到后台
        exchangewindows.exchangewindows(driver)
        sleep(1)
        bstate2 = "已确认,已付款,配货中"
        self.backgoodstate(bstate2)
        sleep(1)
        #执行
        driver.find_element_by_name("ship").click()
        driver.find_element_by_name("delivery_confirmed").click()
        exchangewindows.exchangewindows(driver)
        sleep(1)
        #查看前台状态3
        fstate3 = "已确认,已付款,配货中"
        self.frontgoodstate(fstate3)
        sleep(1)
        exchangewindows.exchangewindows(driver)
        sleep(1)
        #查看后台状态3
        bstate3 = "已分单,已付款,发货中"
        self.backgoodstate(bstate3)
        driver.find_element_by_name("to_delivery").click()
        driver.find_element_by_xpath("/html/body/form/div[1]/table[1]/tbody/tr[3]/td[9]/a[1]").click()
        sleep(1)
        exchangewindows.exchangewindows(driver)
        #查看前台状态4
        fstate4 = "已确认,已付款,配货中"
        self.frontgoodstate(fstate4)
        exchangewindows.exchangewindows(driver)
        #查看后台状态4
        bstate4 = "已分单,已付款,已发货"
        #点击发货，
        driver.find_element_by_name("delivery_confirmed").click()
        sleep(2)
        #查看订单详情
        driver.switch_to_default_content()
        self.searchorder(goodorder)
        check_bstate4 = driver.find_element_by_xpath("/html/body/form/div[1]/table/tbody/tr[3]/td[4]").text
        self.assertEqual(bstate4,check_bstate4,"后台状态4错误")
        driver.find_element_by_name("return").click()
        driver.find_element_by_name("action_note").send_keys("我 要 退货")
        driver.find_element_by_name("submit").click()
        sleep(2)
        #切换到前台，确认收货
        exchangewindows.exchangewindows(driver)
        driver.refresh()
        sleep(3)
#         driver.find_element_by_xpath("/html/body/div[7]/div[2]/div/div/div/table/tbody/tr[2]/td[5]/font/a").click()
#         alert = driver.switch_to_alert()
#         alert.accept()
#         #确认前台信息5
#         fstate5 = "已确认,已付款,收货确认"
#         self.frontgoodstate(fstate5)
#         #切换到后台
#         exchangewindows.exchangewindows(driver)
#         driver.switch_to_default_content()
#         self.searchorder(goodorder)
#         #查看后台状态5
#         bstate5 = "已分单,已付款,收货确认"
#         self.backgoodstate(bstate5)
#         driver.find_element_by_name("return").click()
#         driver.find_element_by_name("action_note").send_keys("我 要 退货")
#         driver.find_element_by_name("return").click()
#         sleep(2)
        #在次切换到前台
#         exchangewindows.exchangewindows(driver)
        #查看前台状态6
        fstate6 = "退货,未付款,未发货"
        self.frontgoodstate(fstate6)
        #切换到后台
        exchangewindows.exchangewindows(driver)
        #查看后台状态6
        bstates6 = "退货,未付款,未发货"
        self.backgoodstate(bstates6)
        driver.find_element_by_name("confirm").click()
        sleep(2)
        #切换到前台
        exchangewindows.exchangewindows(driver)
        #查看前台状态7
        fstate7 = "已确认,未付款,未发货"
        self.frontgoodstate(fstate7)
        #切换到后台
        exchangewindows.exchangewindows(driver)
        #查看后台状态7
        bstate7 = "已确认,未付款,未发货"
        self.backgoodstate(bstate7)   
#         self.goodstate(state1)   
#         driver.find_element_by_link_text("退出").click()

    #添加支付方式
    #到商品列表中查看，并断言，添加商品分类，名称，和品牌结果       
    #后天查看商品状态
#     def goodstate(self,goodorder,status):
#         driver = self.driver2
#         #点击订单列表
#         driver.find_element_by_link_text("订单列表").click()
#         #输入商品编号
#         driver.find_element_by_name("order_sn").send_keys(goodorder)
#         #点击订单状态，设置为
#         status_sel = driver.find_element_by_id("status")
#         sel = Select(status_sel)
#         sel.select_by_value("-1").click()
        
#         #点击搜索
#         driver.find_element_by_xpath("//form[@name='searchForm']/input[3]").click()
#         
#         #提取状态信息
#         check_status = driver.find_element_by_xpath("//form[@name='listForm']/div[1]/table[1]/tbody/tr[3]/td[6]").text
#         self.assertEqual(status, check_status,"商品状态错误")        
    #后台查看前台添加账户信息      
    #前台商品状态   
    def tearDown(self):
        self.driver.quit()        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Ecshop_test("test_zuce"))      
    cur_dir = os.getcwd()#获取当前路径
    sys.path.append(cur_dir)
    print(cur_dir)
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

        
        
        
        
        