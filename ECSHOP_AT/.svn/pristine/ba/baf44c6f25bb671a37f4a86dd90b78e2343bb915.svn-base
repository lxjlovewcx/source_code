#此功能提供前台会员登录及验证
from time import sleep
def test_userlogin(driver,username,password):
    driver.find_element_by_xpath("//a[@href='user.php']").click()
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_class_name("us_Submit").click()
    sleep(5)
    print("登陆成功")