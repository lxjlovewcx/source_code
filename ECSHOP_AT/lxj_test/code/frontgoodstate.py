import unittest
def frontgoodstate(driver,state):
    unitcase = unittest.TestCase()
    driver.refresh()
    check_state = driver.find_element_by_xpath("/html/body/div[7]/div[2]/div/div/div/table/tbody/tr[2]/td[4]").text
    unitcase.assertEqual(state,check_state,"前台状态错误")