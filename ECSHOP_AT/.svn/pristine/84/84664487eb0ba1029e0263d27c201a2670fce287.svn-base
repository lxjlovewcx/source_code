from time import time
def goodclass(driver):
    goodclass = '电子'+str(time()*1000)[6:]
    menu_loc = driver.find_element_by_name("menu-frame")
    driver.switch_to_frame(menu_loc)
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/ul/li[1]/ul/li[3]/a").click()
    driver.switch_to_default_content()
    menu_loc1 = driver.find_element_by_name("main-frame")
    driver.switch_to_frame(menu_loc1)
    driver.find_element_by_xpath("/html/body/h1/span[1]/a").click()
    driver.find_element_by_name("cat_name").send_keys(goodclass)
    driver.find_element_by_name("measure_unit").send_keys('99')
    driver.find_element_by_xpath("//div[@class='button-div']/input[1]").click()
    driver.switch_to_default_content()
    return(goodclass)