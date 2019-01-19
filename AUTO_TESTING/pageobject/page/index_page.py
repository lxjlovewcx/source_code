from selenium.webdriver.common.by import By

class IndexPage():
    top_register_element = [By.XPATH,"//div[@class='head_enroll']/a"]
    
    @staticmethod
    def click_top_register_link(driver):
        driver.find_element(*IndexPage.top_register_element).click()