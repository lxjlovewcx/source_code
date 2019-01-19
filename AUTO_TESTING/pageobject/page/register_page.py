from selenium.webdriver.common.by import By
from base import get_verifycode
from pageobject.page.common_cookie import CommonCookie
from pageobject.page.loging_page import LogingPage
from unittest.case import TestCase

class RegisterPage():
    # 定义注册页面的元素对象
    email_element = [By.NAME,"email"]
    username_element = [By.NAME,"username"]
    password_element = [By.NAME,"password"]
    password1_element = [By.NAME,"password1"]
    proving_element = [By.NAME,"proving"]
    register_button = [By.XPATH,"//*[@id='myform']/div[7]/div/button"]
    agree_element = [By.CLASS_NAME,"checked"]
    validform_info_element = [By.CLASS_NAME,"Validform_info"]
    null_email_tip = "请输入邮箱！"
    
    # 定义注册页面的操作逻辑的方法
    def input_necessary_info(self,driver,email,username,password,password1):
        driver.find_element(*self.email_element).send_keys(email)
        driver.find_element(*self.username_element).send_keys(username)
        driver.find_element(*self.password_element).send_keys(password)
        driver.find_element(*self.password1_element).send_keys(password1)
        session = driver.get_cookie(CommonCookie.session_name)["value"]
        verifycode=get_verifycode(session)
        driver.find_element(*self.proving_element).send_keys(verifycode)
    
    def disagree(self,driver):
        driver.find_element(*self.agree_element).click()
    
    def click_register_button(self,driver):
        driver.find_element(*self.register_button).click()
        
    def check_register_result(self,driver):
        actual_tip = driver.find_element(*LogingPage.success_tip_element).text
        TestCase.assertEqual(TestCase(), LogingPage.register_success_tip, actual_tip)
    
    def check_tip(self,driver,tag):
        actual_tip = driver.find_element(*self.validform_info_element).text
        if tag == "email":
            TestCase.assertEqual(TestCase(), self.null_email_tip, actual_tip)
        