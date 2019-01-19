# -*- coding:UTF-8 -*-
import requests
import unittest,os,sys,time
from report.HTMLTestRunner import HTMLTestRunner
from jn_test.add_goods import add_goods
from asyncio.test_utils import TestCase


def CreatSuite():
    #定义单元测试容器
    suite=unittest.TestSuite()
    suite.addTests(add_goods("test_goods"))
    #suite.addTests(Ecshop.testplace_orders)
                       
    return suite

if __name__ =='__main__':
    suite = CreatSuite()   
    cur_dir = os.getcwd()#获取当前路径
    print(cur_dir)
    sys.path.append(cur_dir)
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    report_folder = cur_dir + os.sep +'report' + os.sep
    filename = report_folder + now + '_result.html'  # 测试报告的路径名
    print(filename)
    fp = open(filename, 'wb')  #以二进制的格式，以写的方式，打开报告文件
    runner = HTMLTestRunner(
        stream=fp,
        title='ECSHOUP_V2.7_AT_Report',
        description='TestCase：',
        )
    #runner = unittest.TextTestRunner()  
    runner.run(suite)
    fp.close()
   