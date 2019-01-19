import unittest
from time import sleep
def denglu_test(driver,username,pwd,email,answerdata): 
        unitcase = unittest.TestCase()     
        driver.find_element_by_xpath("//font[@id='ECS_MEMBERZONE']/a[1]").click()
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").send_keys(pwd)
        driver.find_element_by_name("remember").click()
        driver.find_element_by_name("submit").click()
        sleep(3)