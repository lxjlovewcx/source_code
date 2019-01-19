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
        driver.get(base_url1)
        driver.find_element_by_xpath("//font[@id='ECS_MEMBERZONE']/a[2]/img").click()
        phonenumber = str(time()*1000)[:11]
        email = phonenumber+"@qq.com"
        pwd = str(time()*1000)[:6]
        comfirmpwd = pwd
        msn = email
        qq = phonenumber
        answerdata = "第三方士大夫撒地方似懂非懂舒服的沙发上地方撒都放松放松的方式地方"
        
        first_name=["王","李","张","刘","陈","杨","黄","吴","赵","周","徐","孙","马","朱","胡","林","郭","何","高","罗",
                    "郑","梁","谢","宋","唐","许","邓","冯","韩","曹","曾","彭","萧","蔡","潘","田","董","袁","于","余",
                    "叶","蒋","杜","苏","魏","程","吕","丁","沈","任","姚","卢","傅","钟","姜","崔","谭","廖","范","汪",
                    "陆","金","石","戴","贾","韦","夏","邱","方","侯","邹","熊","孟","秦","白","江","阎","薛","尹","段",
                    "雷","黎","史","龙","陶","贺","顾","毛","郝","龚","邵","万","钱","严","赖","覃","洪","武","莫","孔"]
        second_name=["球","理","捧","堵","描","域","掩","捷排","掉","堆","推","掀","授","教","掏","掠","培","接",
                     "控","探","据","掘","职","基","著","勒","黄","萌","萝","菌","菜萄菊","萍","菠","营","械","梦",
                     "梢","梅","检","梳","梯","桶","救","副","票戚","爽","聋","袭","盛","雪","辅","辆","虚","雀",
                     "堂","常","匙","晨","睁","眯","眼","悬野啦","晚","啄","距","跃","略","蛇","累","唱","患","唯",
                     "崖","崭","崇","圈","铜","铲","银","甜","梨","犁移","笨","笼","笛","符","第","敏","做","袋",
                     "悠","偿","偶偷您","售","停","偏","假","得","衔","盘","船","斜","盒","鸽","悉","欲","彩","领",
                     "脚","脖","脸","脱","象","够","猜","猪","猎","猫","猛馅","馆","凑","减","毫","麻痒痕","廊","康",
                     "庸","鹿","盗","章","竟","商","族","旋","望","率","着","盖","粘","粗","粒","断","剪","兽","清",
                     "添","淋","淹","渠","渐","混","渔","淘","液","淡深婆梁","渗","情","惜","惭","悼","惧","惕","惊",
                     "惨","惯","寇","寄","宿","窑","密","谋","谎","祸","谜","逮","敢","屠","弹","随","蛋","隆","隐",
                     "婚","婶","颈","绩","绪续骑","绳","维","绵","绸绿"]
        third_name=["a","b","c","d","e","f","g","h","i"]
        username = choice(first_name)+choice(second_name)+choice(third_name)
       
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("email").send_keys(email)
        driver.find_element_by_name("password").send_keys(pwd)
        driver.find_element_by_name("confirm_password").send_keys(comfirmpwd)
        driver.find_element_by_name("extend_field1").send_keys(msn)
        driver.find_element_by_name("extend_field2").send_keys(qq)
        driver.find_element_by_name("extend_field3").send_keys(phonenumber)
        driver.find_element_by_name("extend_field4").send_keys(phonenumber)
        driver.find_element_by_name("extend_field5").send_keys(phonenumber)
        sel_question = driver.find_element_by_name("sel_question")
        sel = Select(sel_question)
        sel.select_by_value("friend_birthday")
        driver.find_element_by_name("passwd_answer").send_keys(answerdata)
        driver.find_element_by_name("Submit").click()
        sleep(5)
        check_username = driver.find_element_by_class_name("f4_b").text
        driver.find_element_by_xpath("//div[@class='userMenu']/a[2]/img").click()
        sleep(3)
        check_email = driver.find_element_by_name("email").get_attribute('value')
        check_answerdata = driver.find_element_by_name("passwd_answer").get_attribute('value')
        list1 = [username,email,answerdata]
        check_list1 =[check_username,check_email,check_answerdata]
        sleep(2)
        driver.find_element_by_link_text("退出").click()
        self.assertEqual(list1, check_list1, "注册失败")
        sleep(2)
#         return(username,pwd,email,answerdata,phonenumber)
        
        self.denglu(username,pwd,email,answerdata)
        
        js="window.open('http://172.31.25.125/admin')"
        driver.execute_script(js)
        sleep(1)
        backusername = "lxj"
        backpassword = "lxj123456"
#         list_handles = []
#         list_handles = driver.window_handles()
#         print(driver.window_handles())
        self.exchangewindows()
        self.backlogin(backusername,backpassword)
        #检查后台yonghu
        self.backcheckuser(username,email,phonenumber)
        goodclass = self.goodclass()
        goodbrand = self.goodbrand()
        newgood = self.addnewgood(goodclass,goodbrand)
        sleep(2)
        driver.switch_to_default_content()
        self.checknewgood(newgood,goodclass,goodbrand)
        self.exchangewindows()
        provice = "四川"
        city = '成都'
        area = '锦江区'
#         username = '李雪健'
#         email = '851677798@qq.com'
#         phonenumber = '12345678901'
#         fstate2,fstate3,fstate4,fstate5,fstate6,fstate7 = ","","","","退货,未付款,未发货","已确认,未付款,未发货"
#         bstate2,bstate3,bstate4,bstate5,bstate6 = ","","","已发货","退货,未付款,未发货","已确认,未付款,未发货"
        goodorder = self.buygoods(goodclass,provice,city,area,username,email,phonenumber)
        #前台状态一：
        fstate1 = "已确认,已付款,未发货"
        self.frontgoodstate(fstate1)
        sleep(1)
        #切换到后台
        self.exchangewindows()
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
        self.exchangewindows()
        sleep(1)
        #查看前台状态2
        fstate2 = "已确认,已付款,配货中"
        self.frontgoodstate(fstate2)
        sleep(1)
        #切换窗口到后台
        self.exchangewindows()
        sleep(1)
        bstate2 = "已确认,已付款,配货中"
        self.backgoodstate(bstate2)
        sleep(1)
        #执行
        driver.find_element_by_name("ship").click()
        driver.find_element_by_name("delivery_confirmed").click()
        self.exchangewindows()
        sleep(1)
        #查看前台状态3
        fstate3 = "已确认,已付款,配货中"
        self.frontgoodstate(fstate3)
        sleep(1)
        self.exchangewindows()
        sleep(1)
        #查看后台状态3
        bstate3 = "已分单,已付款,发货中"
        self.backgoodstate(bstate3)
        driver.find_element_by_name("to_delivery").click()
        driver.find_element_by_xpath("/html/body/form/div[1]/table[1]/tbody/tr[3]/td[9]/a[1]").click()
        sleep(1)
        self.exchangewindows()
        #查看前台状态4
        fstate4 = "已确认,已付款,配货中"
        self.frontgoodstate(fstate4)
        self.exchangewindows()
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
        self.exchangewindows()
        driver.refresh()
        sleep(3)
#         driver.find_element_by_xpath("/html/body/div[7]/div[2]/div/div/div/table/tbody/tr[2]/td[5]/font/a").click()
#         alert = driver.switch_to_alert()
#         alert.accept()
#         #确认前台信息5
#         fstate5 = "已确认,已付款,收货确认"
#         self.frontgoodstate(fstate5)
#         #切换到后台
#         self.exchangewindows()
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
#         self.exchangewindows()
        #查看前台状态6
        fstate6 = "退货,未付款,未发货"
        self.frontgoodstate(fstate6)
        #切换到后台
        self.exchangewindows()
        #查看后台状态6
        bstates6 = "退货,未付款,未发货"
        self.backgoodstate(bstates6)
        driver.find_element_by_name("confirm").click()
        sleep(2)
        #切换到前台
        self.exchangewindows()
        #查看前台状态7
        fstate7 = "已确认,未付款,未发货"
        self.frontgoodstate(fstate7)
        #切换到后台
        self.exchangewindows()
        #查看后台状态7
        bstate7 = "已确认,未付款,未发货"
        self.backgoodstate(bstate7)
        
        
        
        
        
        
        
#         self.goodstate(state1)
    def exchangewindows(self):
        driver = self.driver
        curren_hanle = driver.current_window_handle
        for i in driver.window_handles:
            if i != curren_hanle:
                driver.switch_to_window(i)   
    def searchorder(self,goodorder):
        driver = self.driver
        menu_loc = driver.find_element_by_name("menu-frame")
        driver.switch_to_frame(menu_loc)
        driver.find_element_by_link_text("订单查询").click()
        driver.switch_to_default_content()
        menu_loc1 = driver.find_element_by_name("main-frame")
        driver.switch_to_frame(menu_loc1)
        driver.find_element_by_name("order_sn").send_keys(goodorder)
        driver.find_element_by_name("query").click()
        driver.find_element_by_xpath("/html/body/form/div[1]/table[1]/tbody/tr[3]/td[7]/a").click()
        
    def backgoodstate(self,state): 
        driver = self.driver 
        check_state = driver.find_element_by_xpath("/html/body/form/div[1]/table/tbody/tr[3]/td[4]").text
        self.assertEqual(state, check_state, "后台状态正常")
        
    def frontgoodstate(self,state):
        driver = self.driver
        driver.refresh()
        check_state = driver.find_element_by_xpath("/html/body/div[7]/div[2]/div/div/div/table/tbody/tr[2]/td[4]").text
        self.assertEqual(state,check_state,"前台状态错误")
        
    def denglu(self,username,pwd,email,answerdata):
        driver = self.driver
        base_url = self.base_url1
        driver.get(base_url)
        driver.find_element_by_xpath("//font[@id='ECS_MEMBERZONE']/a[1]").click()
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").send_keys(pwd)
        driver.find_element_by_name("remember").click()
        driver.find_element_by_name("submit").click()
        sleep(3)
        #点击用户中心
        driver.find_element_by_link_text("用户中心").click()
        check_username = driver.find_element_by_class_name("f4_b").text
        driver.find_element_by_xpath("//div[@class='userMenu']/a[2]/img").click()
        sleep(3)
        check_email = driver.find_element_by_name("email").get_attribute('value')
        check_answerdata = driver.find_element_by_name("passwd_answer").get_attribute('value')
        list1 = [username,email,answerdata]
        check_list1 =[check_username,check_email,check_answerdata]
        self.assertEqual(list1, check_list1, "注册失败")
#         driver.find_element_by_link_text("退出").click()
    def buygoods(self,goodclass,provice,city,area,username,email,phonenumber):
        driver = self.driver
        driver.find_element_by_link_text("高级搜索").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@id='keywords']").send_keys("苹果")
        search_sel = driver.find_element_by_id("select")
        sel = Select(search_sel)
        sel.select_by_visible_text(goodclass)
        sleep(2)
        
        driver.find_element_by_name("Submit").click()
        driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[3]/div/form/div/div/div/a[3]").click()
        
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[7]/div[1]/table/tbody/tr/td[2]/a/img").click()
        sleep(2)
        #此处需要填写表单数据，
        #修改国籍中国
        country_sel = driver.find_element_by_id("selCountries_0")
        sel = Select(country_sel)
        sel.select_by_value("1")
        #修改省份
        provice_sel = driver.find_element_by_id("selProvinces_0")
        sel = Select(provice_sel)
        sel.select_by_visible_text(provice)   
        #修改市
        city_sel = driver.find_element_by_id("selCities_0")
        sel = Select(city_sel)
        sel.select_by_visible_text(city)   
        #修改区域
        area_sel = driver.find_element_by_id("selDistricts_0")
        sel = Select(area_sel)
        sel.select_by_visible_text(area) 
        #添加收货人姓名
        driver.find_element_by_name("consignee").send_keys(username)
        #添加email
        driver.find_element_by_name("email").send_keys(email)
        #添加详细地址
        driver.find_element_by_name("address").send_keys("按时交付凯撒分开")
        
        #添加电话
        driver.find_element_by_name("tel").send_keys(phonenumber)
        #点击配送到这个地址
        driver.find_element_by_name("Submit").click()
        #后台已经修改好了配送方式和支付方式
        #选择上门取货送货方式
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[7]/form/div[5]/table/tbody/tr[2]/td[1]/input").click()
        sleep(2)
#         #选择余额付款支付方式
#         driver.find_element_by_xpath("/html/body/div[7]/form/div[7]/table/tbody/tr[2]/td[1]/input")
        #选择货到付款支付方式
        driver.find_element_by_xpath("/html/body/div[7]/form/div[7]/table/tbody/tr[2]/td[1]/input").click()
        #点击提交订单
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[7]/form/div[11]/div[2]/input[1]").click()
        sleep(2)
        #记住订单号：
        goodorder = driver.find_element_by_xpath("/html/body/div[7]/div/h6/font").text
        sleep(2)
        driver.find_element_by_link_text("用户中心").click()
        driver.find_element_by_xpath("//div[@class='userMenu']/a[3]/img").click()
        
        
        #后台登陆函数
        return(goodorder)
    def backlogin(self,backusername,backpassword):
        driver = self.driver
        base_url2 = self.base_url2
        driver.get(base_url2)
        driver.find_element_by_name("username").send_keys(backusername)
        driver.find_element_by_name("password").send_keys(backpassword)
        driver.find_element_by_class_name("button").click()
    #添加商品分类
    def goodclass(self):
        driver = self.driver
        goodclass = '电子'+str(time()*1000)[6:]
        menu_loc = driver.find_element_by_name("menu-frame")
        driver.switch_to_frame(menu_loc)
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/ul/li[1]/ul/li[3]/a").click()
        driver.switch_to_default_content()
        menu_loc1 = driver.find_element_by_name("main-frame")
        driver.switch_to_frame(menu_loc1)
        driver.find_element_by_xpath("/html/body/h1/span[1]/a").click()
        driver.find_element_by_name("cat_name").send_keys(goodclass)
        driver.find_element_by_name("measure_unit").send_keys('99')
        driver.find_element_by_xpath("//div[@class='button-div']/input[1]").click()
        driver.switch_to_default_content()
        return(goodclass)
        
    #添加商品品牌
    def goodbrand(self):
        driver = self.driver
        goodbrand = 'ap'+str(time()*1000)[6:]
        menu_loc = driver.find_element_by_name("menu-frame")
        driver.switch_to_frame(menu_loc)
        driver.find_element_by_link_text("商品品牌").click()
        driver.switch_to_default_content()
        menu_loc1 = driver.find_element_by_name("main-frame")
        driver.switch_to_frame(menu_loc1) 
        sleep(2)  
        driver.find_element_by_link_text("添加品牌").click()
        sleep(2)
        driver.find_element_by_name("brand_name").send_keys(goodbrand)
        driver.find_element_by_xpath("/html/body/div[1]/form/table/tbody/tr[7]/td/input[1]").click()
        driver.switch_to_default_content()
        return(goodbrand)
     
        
    
    #添加新商品
    def addnewgood(self,goodclass,goodbrand):
        driver = self.driver
        newgood = 'new苹果'+str(time()*1000)[:6]
        menu_loc = driver.find_element_by_name("menu-frame")
        driver.switch_to_frame(menu_loc)
        driver.find_element_by_link_text("添加新商品").click()
        driver.switch_to_default_content()
        menu_loc1 = driver.find_element_by_name("main-frame")
        driver.switch_to_frame(menu_loc1) 
        sleep(2)  
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/table[1]/tbody/tr[1]/td[2]/input[1]").send_keys(newgood)
        goodclass_sel = driver.find_element_by_name("cat_id")
        sleep(2)
        sel=Select(goodclass_sel)
        sel.select_by_visible_text(goodclass)
        goodbrand_sel = driver.find_element_by_name("brand_id")
        sel = Select(goodbrand_sel)
        sel.select_by_visible_text(goodbrand)
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/table[1]/tbody/tr[1]/td[2]/input[1]").send_keys(newgood)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/div/input[2]").click()

        sleep(2)
        return(newgood)
    #添加支付方式
    def addzifufangsi(self,goodbrand):
        driver = self.driver
        menu_loc = driver.find_element_by_name("menu-frame")
        driver.switch_to_frame(menu_loc)
        driver.find_element_by_link_text("配送方式").click()
        driver.switch_to_default_content()
        menu_loc1 = driver.find_element_by_name("main-frame")
        driver.switch_to_frame(menu_loc1) 
        sleep(2)  
        driver.find_element_by_link_text("添加品牌").click()
        sleep(2)
        driver.find_element_by_name("brand_name").send_keys(goodbrand)
        driver.find_element_by_xpath("/html/body/div[1]/form/table/tbody/tr[7]/td/input[1]").click()
        driver.switch_to_default_content()
        
    #到商品列表中查看，并断言，添加商品分类，名称，和品牌结果
    def checknewgood(self,newgood,goodclass,goodbrand):
        driver = self.driver
        
        menu_loc = driver.find_element_by_name("menu-frame")
        driver.switch_to_frame(menu_loc)
        driver.find_element_by_link_text("商品列表").click()
        driver.switch_to_default_content()
        menu_loc1 = driver.find_element_by_name("main-frame")
        driver.switch_to_frame(menu_loc1) 
        driver.find_element_by_name("keyword").send_keys(newgood)
        driver.find_element_by_xpath("/html/body/div[1]/form/input[2]").click()
        driver.find_element_by_xpath("/html/body/form/div[1]/table[1]/tbody/tr[3]/td[11]/a[2]/img").click()
        sleep(2)
        check_newgood = driver.find_element_by_name("goods_name").get_attribute("value")
#        driver.find_element_by_xpath("//select[]")("cat_id")
#         sel = Select(goodclass_sel)
#         check_goodclass = sel.select_by_selected("true").text
#         goodbrand_sel = driver.find_element_by_name("brand_id")
#         sel = Select(goodbrand_sel)
#         check_goodbrand = sel.select_by_selected("true").text
#         list1 = [newgood,goodclass,goodbrand]
#         list2 = [check_newgood,check_goodclass,check_goodbrand]
        self.assertIn(newgood, check_newgood, "后台添加商品失败")
        
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
    def backcheckuser(self,username,email,phonenumber):
        driver = self.driver
        menu_loc = driver.find_element_by_name("menu-frame")
        driver.switch_to_frame(menu_loc)
        driver.find_element_by_link_text("会员列表").click()
        driver.switch_to_default_content()
        menu_loc1 = driver.find_element_by_name("main-frame")
        driver.switch_to_frame(menu_loc1) 
        driver.find_element_by_name("keyword").send_keys(username)
        driver.find_element_by_xpath("/html/body/div[1]/form/input[4]").click()
        driver.find_element_by_xpath("/html/body/form/div/table/tbody/tr[3]/td[10]/a[1]/img").click()
        check_username = driver.find_element_by_xpath("/html/body/div[1]/form/table/tbody/tr[1]/td[2]").text
        check_email = driver.find_element_by_name("email").get_attribute("value")
        check_phonenumber = driver.find_element_by_name("extend_field3").get_attribute("value")
        list1 = [username,email,phonenumber]
        list2 = [check_username,check_email,check_phonenumber]
        self.assertEqual(list1, list2, "后台账户确认失败")
        driver.find_element_by_xpath("/html/body/div[1]/form/table/tbody/tr[18]/td/input[1]").click()
        driver.switch_to_default_content()
        
        
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

    report_folder = cur_dir + os.sep +r'lxj_test\report' + os.sep
    filename = report_folder + now + '_result.html'  # 测试报告的路径名
    print(filename)
    fp = open(filename, 'wb')  #以二进制的格式，以写的方式，打开报告文件
    runner = HTMLTestRunner(
        stream=fp,
        title='接口自动化测试报告',
        description='用例执行情况：',
        )
    #runner = unittest.TextTestRunner()  
    runner.run(suite)
#     

        
        
        
        
        