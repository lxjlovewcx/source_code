import unittest,os,sys,time
from selenium import webdriver
from lxj_test import zuce_test, denglu_test, backlogin_test, goodclass_test
from lxj_test.HTMLTestRunner import HTMLTestRunner



class ECshop_test(unittest.TestCase):
    def setUp(self):
        self.driver1 = webdriver.Firefox()
        self.driver2 = webdriver.Firefox()
        self.base_url1 = "http://172.31.25.125/"
        self.base_url2 = "http://172.31.25.125/admin"
    def test_1(self):
        username,pwd,email,answerdata,phonenumber = zuce_test.zuce_test(self.driver1,self.base_url1)
        self.driver1.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li/font/font/a[2]")
#         denglu_test.denglu_test(self.driver1,self.base_url1,username, pwd, email, answerdata)
        backusername = "lxj"
        backpassword = "lxj123456"
        backlogin_test.test_backlogin(self.driver2,self.base_url2,backusername,backpassword)
        goodclass_test.test_goodclass(self.driver2)
    def tearDown(self):
        self.driver1.quit()
        self.driver2.quit()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(ECshop_test("test_1"))     
#     suite.addTest(ECshop_test("test_2")) 
    cur_dir = os.getcwd()#获取当前路径
    sys.path.append(cur_dir)
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    report_folder = cur_dir + os.sep +'report' + os.sep
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