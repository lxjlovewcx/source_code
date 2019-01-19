import unittest,os,sys,time
from selenium import webdriver
from sl_test.ECSHOP.admin_login import test_adminlogin
from sl_test.ECSHOP.user_login import test_userlogin
from sl_test.ECSHOP.verifying_change import test_verifychange
from sl_test.ECSHOP.charge import test_charge
from time import  sleep
from sl_test.ECSHOP.verifying_money import test_verifyingmoney
from sl_test.ECSHOP.change_userinformation import test_userinformation
from sl_test.ECSHOP.HTMLTestRunner import HTMLTestRunner

class ECHOP_MAIN(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.admin_url = "http://172.31.25.125/admin"
        self.base_url = "http://172.31.25.125"
        self.driver.set_script_timeout(30)
        self.driver.set_page_load_timeout(30)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        
    def test_main(self):
        driver = self.driver
        admin_username="admin"
        admin_password="zxc123456789"
        username = "shenliang"
        password = "1234567" 
        sex_no = 1  
        birth_year = "1992"
        birth_month = "12"
        birth_day = "31"
        driver.get(self.admin_url)
        front_page="window.open('"+self.base_url+"')"
        driver.execute_script(front_page)
        handles = driver.window_handles
        driver.switch_to_window(handles[1])
        test_userlogin(driver, username, password)
        b_money,b_jifen, q_number, b_number, j_number, p_number, msn, email = test_userinformation(driver, birth_year, birth_month, birth_day, sex_no)
        driver.switch_to_window(handles[0])
        test_adminlogin(driver, admin_username, admin_password)
        test_verifychange(driver, username, email, sex_no, msn, q_number, b_number, j_number, p_number, birth_year, birth_month, birth_day)
        level = test_charge(driver, username, actual_value = 1000)
        driver.switch_to_window(handles[1])
        test_verifyingmoney(driver,b_money,b_jifen,level,actual_value=1000)

        
        

        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(ECHOP_MAIN("test_main"))     
    cur_dir = os.getcwd()#获取当前路径
    sys.path.append(cur_dir)
    now = time.strftime("%Y-%m-%d-%H_%M_%S")
    report_folder = cur_dir + os.sep +'report' + os.sep
    filename = report_folder + now + '_result.html'  # 测试报告的路径名
    print(filename)
    fp = open(filename, 'wb')  #以二进制的格式，以写的方式，打开报告文件
    runner = HTMLTestRunner(
        stream=fp,
        title='自动化测试报告',
        description='用例执行情况：',
        )
    #runner = unittest.TextTestRunner()  
    runner.run(suite)
    