def searchorder(driver,goodorder):
    menu_loc = driver.find_element_by_name("menu-frame")
    driver.switch_to_frame(menu_loc)
    driver.find_element_by_link_text("订单查询").click()
    driver.switch_to_default_content()
    menu_loc1 = driver.find_element_by_name("main-frame")
    driver.switch_to_frame(menu_loc1)
    driver.find_element_by_name("order_sn").send_keys(goodorder)
    driver.find_element_by_name("query").click()
    driver.find_element_by_xpath("/html/body/form/div[1]/table[1]/tbody/tr[3]/td[7]/a").click()