from selenium.webdriver.support.select import Select

def test_buygoods(self,Select,driver,goodclass,provice,city,area,username,email,phonenumber):
        driver = self.driver
        driver.find_element_by_name("keywords").send_keys(goodclass)
        driver.find_element_by_xpath("//div[@id='show_best_area']/div[1]/a[1]/img").click()
        driver.find_element_by_xpath("/html/body/div[7]/div[1]/table/tbody/tr/td[2]/a/img").click()
        driver.find_element_by_xpath("/html/body/div[7]/form/div[3]/h6/a").click()
        #此处需要填写表单数据，
        #修改国籍中国
        country_sel = driver.find_element_by_id("selCountries_0")
        sel = Select(country_sel)
        sel.select_by_value("1")
        #修改省份
        provice_sel = driver.find_element_by_id("selProvinces_0")
        sel = Select(provice_sel)
        sel.select_by_visible_text(provice)   
        #修改市
        city_sel = driver.find_element_by_id("selCities_0")
        sel = Select(city_sel)
        sel.select_by_visible_text(city)   
        #修改区域
        area_sel = driver.find_element_by_id("selDistricts_0")
        sel = Select(area_sel)
        sel.select_by_visible_text(area) 
        #添加收货人姓名
        driver.find_element_by_name("consignee").setAttribute('value',username)
        #添加email
        driver.find_element_by_name("email").setAttribute('value',email)
        #添加详细地址
        driver.find_element_by_name("address").setAttribute('value',"按时交付凯撒分开")
        
        #添加电话
        driver.find_element_by_name("tel").setAttribute('value',phonenumber)
        #点击配送到这个地址
        driver.find_element_by_name("Submit").click()
        #后台已经修改好了配送方式和支付方式
        #选择上门取货送货方式
        driver.find_element_by_name("shipping").click()
        #选择货到付款支付方式
        driver.find_element_by_xpath("/html/body/div[7]/form/div[7]/table/tbody/tr[3]/td[1]/input")
        #选择余额付款支付方式
        driver.find_element_by_xpath("/html/body/div[7]/form/div[7]/table/tbody/tr[2]/td[1]/input")
        #点击提交订单
        driver.find_element_by_xpath("/html/body/div[7]/form/div[11]/div[2]/input[1]").click()
        #记住订单号：
        driver.find_element_by_xpath("/html/body/div[7]/div/h6/font").text