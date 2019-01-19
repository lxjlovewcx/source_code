from time import sleep
import unittest

def denglu_test(driver,base_url,username,pwd,email,answerdata):
        driver.get(base_url)
        driver.find_element_by_xpath("//font[@id='ECS_MEMBERZONE']/a[1]").click()
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").send_keys(pwd)
        driver.find_element_by_name("remember").click()
        driver.find_element_by_name("submit").click()
        check_username = driver.find_element_by_class_name("f4_b").text
        driver.find_element_by_xpath("//div[@class='userMenu']/a[2]/img").click()
        sleep(3)
        check_email = driver.find_element_by_name("email").get_attribute('value')
        check_answerdata = driver.find_element_by_name("passwd_answer").get_attribute('value')
        list1 = [username,email,answerdata]
        check_list1 =[check_username,check_email,check_answerdata]
        unittest.TestCase.assertEqual(unittest.TestCase(),list1, check_list1, "注册失败")
        driver.find_element_by_link_text("退出")