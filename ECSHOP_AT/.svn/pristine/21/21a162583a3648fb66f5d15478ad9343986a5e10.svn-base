import unittest
def backgoodstate(driver,state): 
    unitcase = unittest.TestCase()
    check_state = driver.find_element_by_xpath("/html/body/form/div[1]/table/tbody/tr[3]/td[4]").text
    unitcase.assertEqual(state, check_state, "后台状态正常")