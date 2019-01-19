from time import time,sleep
def goodbrand(driver):
    goodbrand = 'ap'+str(time()*1000)[6:]
    menu_loc = driver.find_element_by_name("menu-frame")
    driver.switch_to_frame(menu_loc)
    driver.find_element_by_link_text("商品品牌").click()
    driver.switch_to_default_content()
    menu_loc1 = driver.find_element_by_name("main-frame")
    driver.switch_to_frame(menu_loc1) 
    sleep(2)  
    driver.find_element_by_link_text("添加品牌").click()
    sleep(2)
    driver.find_element_by_name("brand_name").send_keys(goodbrand)
    driver.find_element_by_xpath("/html/body/div[1]/form/table/tbody/tr[7]/td/input[1]").click()
    driver.switch_to_default_content()
    return(goodbrand)