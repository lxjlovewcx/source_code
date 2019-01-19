#此功能提供后台管理员登录及验证
from unittest import TestCase
from time import sleep

def test_adminlogin(driver,admin_username,admin_password):
    driver.find_element_by_name("username").send_keys(admin_username)
    driver.find_element_by_name("password").send_keys(admin_password)
    driver.find_element_by_class_name("button").click()
    driver.switch_to_frame("header-frame")
    driver.find_element_by_link_text("个人设置").click()
    driver.switch_to_default_content()
    driver.switch_to_frame("main-frame")   
    actual_name = driver.find_element_by_name("user_name").get_attribute("value")
    sleep(1)
    TestCase.assertEqual(TestCase(),actual_name, admin_username)
    driver.switch_to_default_content()
    driver.switch_to_frame("header-frame")
    driver.find_element_by_link_text("起始页").click()
    driver.switch_to_default_content()
         



