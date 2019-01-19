from unittest import TestCase
from time import sleep
from selenium.webdriver.support.select import Select
from select import select

def test_verifychange(driver,username,email,sex_no,msn,q_number,b_number,j_number,p_number,birth_year,birth_month,birth_day):
    driver.switch_to_frame("menu-frame")
    driver.find_element_by_link_text("会员列表").click()
    driver.switch_to_default_content()
    driver.switch_to_frame("main-frame")
    driver.find_element_by_name("keyword").send_keys(username)
    driver.find_element_by_xpath("//input[@type='submit']").click()
    sleep(1)
    driver.find_element_by_xpath("//a[@title='编辑']").click()
    actual_name = driver.find_element_by_name("username").get_attribute("value")
    TestCase.assertEqual(TestCase(), actual_name, username)
    actual_mail = driver.find_element_by_name("email").get_attribute("value")
    TestCase.assertEqual(TestCase(), actual_mail, email)
    print("前后台邮件对比一致")
    actual_msn = driver.find_element_by_name("extend_field1").get_attribute("value")
    TestCase.assertEqual(TestCase(), actual_msn, msn)
    print("前后台MSN对比一致")
    a_qnumber = driver.find_element_by_name("extend_field2").get_attribute("value")
    TestCase.assertEqual(TestCase(), a_qnumber, q_number)
    print("前后台QQ对比一致")
    a_bnumber = driver.find_element_by_name("extend_field3").get_attribute("value")
    TestCase.assertEqual(TestCase(), a_bnumber, b_number)
    print("前后台办公电话对比一致")
    a_jnumber = driver.find_element_by_name("extend_field4").get_attribute("value")
    TestCase.assertEqual(TestCase(), a_jnumber, j_number)
    print("前后台家庭电话对比一致")
    a_pnumber = driver.find_element_by_name("extend_field5").get_attribute("value")
    TestCase.assertEqual(TestCase(), a_pnumber, p_number)
    print("前后台手机对比一致")
    actual_sex= driver.find_element_by_xpath("//input[@checked]").get_attribute("value")
    TestCase.assertEqual(TestCase(), actual_sex, str(sex_no)) 
    print("前后台性别对比一致")
    actual_years = driver.find_element_by_name("birthdayYear")
    actual_year  =  Select(actual_years)
    for select in actual_year.all_selected_options :
        a_year = select.text
    TestCase.assertCountEqual(TestCase(), a_year, birth_year)
    actual_months = driver.find_element_by_name("birthdayMonth")
    actual_month  =  Select(actual_months)
    for select in actual_month.all_selected_options :
        a_month = select.text
    TestCase.assertCountEqual(TestCase(), a_month, birth_month)
    actual_days = driver.find_element_by_name("birthdayDay")
    actual_day  =  Select(actual_days)
    for select in actual_day.all_selected_options :
        a_day = select.text
    TestCase.assertCountEqual(TestCase(), a_day, birth_day)
    print("出生日期对比一致") 
    driver.switch_to_default_content()
    driver.switch_to_frame("header-frame")
    driver.find_element_by_link_text("起始页").click()
    driver.switch_to_default_content()
    
    