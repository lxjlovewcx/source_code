import unittest 
from time import sleep
from unittest import TestCase
def logining(driver,base_url,user,pw):
    driver.get(base_url)
    driver.find_element_by_xpath("//img[@src='themes/default/images/bnt_log.gif']").click()
    driver.find_element_by_name("username").send_keys(user)
    driver.find_element_by_name("password").send_keys(pw)
    driver.find_element_by_name("submit").click()
    sleep(1)
    username=driver.find_element_by_xpath("//font[@class='f4_b']").text
    TestCase.assertEqual(TestCase(),user, username)
   
                