from unittest import TestCase
from time import sleep
from selenium.webdriver.support.select import Select

def test_charge(driver,username,actual_value):
    driver.switch_to_frame("menu-frame")
    driver.find_element_by_link_text("会员列表").click()
    driver.switch_to_default_content()
    driver.switch_to_frame("main-frame")
    driver.find_element_by_name("keyword").send_keys(username)
    driver.find_element_by_xpath("//input[@type='submit']").click()
    sleep(1)
    driver.find_element_by_xpath("//a[@title='编辑']").click()
    driver.find_element_by_link_text("[ 查看明细 ]").click()
    driver.find_element_by_link_text("调节会员帐户").click()
    driver.find_element_by_name("change_desc").send_keys("buy some thing !!!!!")
    charge_options = driver.find_element_by_name("add_sub_user_money")  
    select_option = Select(charge_options)  
    select_option.select_by_visible_text("增加")
    driver.find_element_by_name("user_money").send_keys(actual_value) 
    print("充值成功") #添加实际值的金额
    form = driver.find_element_by_name("theForm")
    all_forms = form.find_elements_by_tag_name("tr")
    level_form = all_forms[4].text
    start_nuber = level_form.find("当前值")
    level =int(level_form[start_nuber+4:])
    if level > 0 :
        level_options = driver.find_element_by_name("add_sub_rank_points")
        level_option = Select(level_options)  
        level_option.select_by_visible_text("减少")
    driver.find_element_by_name("rank_points").send_keys(level)
    driver.find_element_by_class_name("button").click()
    driver.switch_to_default_content()
    driver.switch_to_frame("header-frame")
    driver.find_element_by_link_text("起始页").click()
    driver.switch_to_default_content()
    print("积分归零成功")
    return(level)