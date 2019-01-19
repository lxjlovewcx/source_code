import unittest
from time import time,sleep
def checknewgood(driver,newgood,goodclass,goodbrand):
    unitcase = unittest.TestCase()
    menu_loc = driver.find_element_by_name("menu-frame")
    driver.switch_to_frame(menu_loc)
    driver.find_element_by_link_text("商品列表").click()
    driver.switch_to_default_content()
    menu_loc1 = driver.find_element_by_name("main-frame")
    driver.switch_to_frame(menu_loc1) 
    driver.find_element_by_name("keyword").send_keys(newgood)
    driver.find_element_by_xpath("/html/body/div[1]/form/input[2]").click()
    driver.find_element_by_xpath("/html/body/form/div[1]/table[1]/tbody/tr[3]/td[11]/a[2]/img").click()
    sleep(2)
    check_newgood = driver.find_element_by_name("goods_name").get_attribute("value")
#        driver.find_element_by_xpath("//select[]")("cat_id")
#         sel = Select(goodclass_sel)
#         check_goodclass = sel.select_by_selected("true").text
#         goodbrand_sel = driver.find_element_by_name("brand_id")
#         sel = Select(goodbrand_sel)
#         check_goodbrand = sel.select_by_selected("true").text
#         list1 = [newgood,goodclass,goodbrand]
#         list2 = [check_newgood,check_goodclass,check_goodbrand]
    unitcase.assertIn(newgood, check_newgood, "后台添加商品失败")