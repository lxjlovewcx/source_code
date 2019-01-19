from time import sleep
import unittest

def denglu_test(driver,username,pwd,email,answerdata): 
        unitcase = unittest.TestCase()     
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
        unitcase.assertEqual(list1, check_list1, "注册失败")