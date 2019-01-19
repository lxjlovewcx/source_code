from time import time,sleep
from selenium.webdriver.support.select import Select
def addnewgood(driver,goodclass,goodbrand):
    newgood = 'new苹果'+str(time()*1000)[:6]
    menu_loc = driver.find_element_by_name("menu-frame")
    driver.switch_to_frame(menu_loc)
    driver.find_element_by_link_text("添加新商品").click()
    driver.switch_to_default_content()
    menu_loc1 = driver.find_element_by_name("main-frame")
    driver.switch_to_frame(menu_loc1) 
    sleep(2)  
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/table[1]/tbody/tr[1]/td[2]/input[1]").send_keys(newgood)
    goodclass_sel = driver.find_element_by_name("cat_id")
    sleep(2)
    sel = Select(goodclass_sel)
    sel.select_by_visible_text(goodclass)
    goodbrand_sel = driver.find_element_by_name("brand_id")
    sel = Select(goodbrand_sel)
    sel.select_by_visible_text(goodbrand)
    sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/table[1]/tbody/tr[1]/td[2]/input[1]").send_keys(newgood)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/div/input[2]").click()
    
    sleep(2)
    return(newgood)