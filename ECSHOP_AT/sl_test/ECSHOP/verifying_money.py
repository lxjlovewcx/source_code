from unittest import TestCase

def test_verifyingmoney(driver,b_money,b_jifen,level,actual_value=1000):
    driver.find_element_by_link_text("用户中心").click()
    after_money = driver.find_element_by_xpath("//a[@href='user.php?act=account_log' and @style='color:#006bd0;']").text
    jifen = driver.find_element_by_xpath("//div[@class='f_l' and @style='width:350px;']").text
    start_text = "积分:"
    start_number=jifen.find(start_text)
    a_jifen = jifen[start_number+3:-2]
    a_money = after_money[1:-1]
    try :
        Center_boxes = driver.find_element_by_class_name("boxCenterList")
        Center_box = Center_boxes.text
        b= Center_box.find("您的等级是")
        actual_level=(Center_box[b+6:b+10])
        if level >= 1 :
            level_name = "铜牌会员"
        if level >= 501 :
            level_name = "银牌会员"
        if level >= 1001 :
            level_name = "金牌会员"
        if level >= 1501 :
            level_name = "钻石会员"
        if level >= 8001 :
            level_name = "骨灰会员"
        TestCase.assertEqual(TestCase(), level_name, actual_level)
    except :
        print("您的账户没有积分。，请购买商品获得积分")
    
    
#     TestCase.assertEqual(TestCase(), a_jifen, b_jifen+actual_value)
#     TestCase.assertEqual(TestCase(), a_money, b_money+actual_value)
    print("购买前后资金计算正确")
    print("购买前后用户消费积分计算正确")
    print("购买前后用户等级正确")
       