from time import sleep,time
from selenium.webdriver.support.select import Select

def test_userinformation(driver,birth_year,birth_month,birth_day,sex_no):
    email = str(time())+"@qq.com"
    msn = str(time())+"@msn.com"
    q_number=str(time())[0:9]
    b_number=str(time())[0:10]
    j_number=str(time())[0:10]
    p_number=str(time())[0:10]
    answer = str(time())
    driver.find_element_by_link_text("用户中心").click()
    driver.find_element_by_link_text("用户信息").click()
    years = driver.find_element_by_name("birthdayYear")
    year = Select(years)
    year.select_by_visible_text(birth_year)
    months = driver.find_element_by_name("birthdayMonth")
    month = Select(months)
    month.select_by_visible_text(birth_month)
    days = driver.find_element_by_name("birthdayDay")
    day = Select(days)
    day.select_by_visible_text(birth_day)
    sex = driver.find_elements_by_name("sex")
    sex[sex_no].click()
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("extend_field1").clear()
    driver.find_element_by_name("extend_field1").send_keys(msn)
    driver.find_element_by_name("extend_field2").clear()
    driver.find_element_by_name("extend_field2").send_keys(q_number)
    driver.find_element_by_name("extend_field3").clear()
    driver.find_element_by_name("extend_field3").send_keys(b_number)
    driver.find_element_by_name("extend_field4").clear()
    driver.find_element_by_name("extend_field4").send_keys(j_number)
    driver.find_element_by_name("extend_field5").clear()
    driver.find_element_by_name("extend_field5").send_keys(p_number)
    questions = driver.find_element_by_name("sel_question")
    select_question = Select(questions)
    select_question.select_by_index(1)
    driver.find_element_by_name("passwd_answer").clear()
    driver.find_element_by_name("passwd_answer").send_keys(answer)
    driver.find_element_by_class_name("bnt_blue_1").click()
    sleep(1)
    driver.find_element_by_link_text("查看我的个人信息").click()
    driver.find_element_by_link_text("欢迎页").click()
    sleep(2)
    before_money = driver.find_element_by_xpath("//a[@href='user.php?act=account_log' and @style='color:#006bd0;']").text
    jifen = driver.find_element_by_xpath("//div[@class='f_l' and @style='width:350px;']").text
    start_text = "积分:"
    start_number=jifen.find(start_text)
    b_jifen = jifen[start_number+3:-2]
    print("获取购买前积分成功")
    b_money = before_money[1:-1]
    print("获取购买前金额成功")
    print("前台修改用户资料成功")

    return(b_money,b_jifen, q_number, b_number, j_number, p_number, msn, email)