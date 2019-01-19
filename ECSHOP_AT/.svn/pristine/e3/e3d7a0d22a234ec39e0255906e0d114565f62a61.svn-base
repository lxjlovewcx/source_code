import unittest
def backcheckuser(driver,username,email,phonenumber):
        unitcase = unittest.TestCase()
        menu_loc = driver.find_element_by_name("menu-frame")
        driver.switch_to_frame(menu_loc)
        driver.find_element_by_link_text("会员列表").click()
        driver.switch_to_default_content()
        menu_loc1 = driver.find_element_by_name("main-frame")
        driver.switch_to_frame(menu_loc1) 
        driver.find_element_by_name("keyword").send_keys(username)
        driver.find_element_by_xpath("/html/body/div[1]/form/input[4]").click()
        driver.find_element_by_xpath("/html/body/form/div/table/tbody/tr[3]/td[10]/a[1]/img").click()
        check_username = driver.find_element_by_xpath("/html/body/div[1]/form/table/tbody/tr[1]/td[2]").text
        check_email = driver.find_element_by_name("email").get_attribute("value")
        check_phonenumber = driver.find_element_by_name("extend_field3").get_attribute("value")
        list1 = [username,email,phonenumber]
        list2 = [check_username,check_email,check_phonenumber]
        unitcase.assertEqual(list1, list2, "后台账户确认失败")
        driver.find_element_by_xpath("/html/body/div[1]/form/table/tbody/tr[18]/td/input[1]").click()
        driver.switch_to_default_content()