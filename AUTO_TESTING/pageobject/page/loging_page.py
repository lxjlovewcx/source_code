from selenium.webdriver.common.by import By


class LogingPage(object):
    '''
    提示页所包含的页面元素与操作逻辑的方法
    '''
    success_tip_element = [By.CLASS_NAME,"green"]
    register_success_tip = "注册成功"
    