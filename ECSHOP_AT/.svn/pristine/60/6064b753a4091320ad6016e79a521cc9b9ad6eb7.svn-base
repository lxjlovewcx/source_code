from time import time
from random import choice
from selenium.webdriver.support.select import Select
from time import sleep
import unittest

def zuce_test(driver,base_url):
        driver.get(base_url)
        driver.find_element_by_xpath("//font[@id='ECS_MEMBERZONE']/a[2]/img").click()
        phonenumber = str(time()*1000)[:11]
        email = phonenumber+"@qq.com"
        pwd = str(time()*1000)[:6]
        comfirmpwd = pwd
        msn = email
        qq = phonenumber
        answerdata = "第三方士大夫撒地方似懂非懂舒服的沙发上地方撒都放松放松的方式地方"
        
        first_name=["王","李","张","刘","陈","杨","黄","吴","赵","周","徐","孙","马","朱","胡","林","郭","何","高","罗",
                    "郑","梁","谢","宋","唐","许","邓","冯","韩","曹","曾","彭","萧","蔡","潘","田","董","袁","于","余",
                    "叶","蒋","杜","苏","魏","程","吕","丁","沈","任","姚","卢","傅","钟","姜","崔","谭","廖","范","汪",
                    "陆","金","石","戴","贾","韦","夏","邱","方","侯","邹","熊","孟","秦","白","江","阎","薛","尹","段",
                    "雷","黎","史","龙","陶","贺","顾","毛","郝","龚","邵","万","钱","严","赖","覃","洪","武","莫","孔"]
        second_name=["球","理","捧","堵","描","域","掩","捷排","掉","堆","推","掀","授","教","掏","掠","培","接",
                     "控","探","据","掘","职","基","著","勒","黄","萌","萝","菌","菜萄菊","萍","菠","营","械","梦",
                     "梢","梅","检","梳","梯","桶","救","副","票戚","爽","聋","袭","盛","雪","辅","辆","虚","雀",
                     "堂","常","匙","晨","睁","眯","眼","悬野啦","晚","啄","距","跃","略","蛇","累","唱","患","唯",
                     "崖","崭","崇","圈","铜","铲","银","甜","梨","犁移","笨","笼","笛","符","第","敏","做","袋",
                     "悠","偿","偶偷您","售","停","偏","假","得","衔","盘","船","斜","盒","鸽","悉","欲","彩","领",
                     "脚","脖","脸","脱","象","够","猜","猪","猎","猫","猛馅","馆","凑","减","毫","麻痒痕","廊","康",
                     "庸","鹿","盗","章","竟","商","族","旋","望","率","着","盖","粘","粗","粒","断","剪","兽","清",
                     "添","淋","淹","渠","渐","混","渔","淘","液","淡深婆梁","渗","情","惜","惭","悼","惧","惕","惊",
                     "惨","惯","寇","寄","宿","窑","密","谋","谎","祸","谜","逮","敢","屠","弹","随","蛋","隆","隐",
                     "婚","婶","颈","绩","绪续骑","绳","维","绵","绸绿"]
        username = choice(first_name)+choice(second_name)+"lsm"
       
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("email").send_keys(email)
        driver.find_element_by_name("password").send_keys(pwd)
        driver.find_element_by_name("confirm_password").send_keys(comfirmpwd)
        driver.find_element_by_name("extend_field1").send_keys(msn)
        driver.find_element_by_name("extend_field2").send_keys(qq)
        driver.find_element_by_name("extend_field3").send_keys(phonenumber)
        driver.find_element_by_name("extend_field4").send_keys(phonenumber)
        driver.find_element_by_name("extend_field5").send_keys(phonenumber)
        sel_question = driver.find_element_by_name("sel_question")
        sel = Select(sel_question)
        sel.select_by_value("friend_birthday")
        driver.find_element_by_name("passwd_answer").send_keys(answerdata)
        driver.find_element_by_name("Submit").click()
        sleep(5)
        check_username = driver.find_element_by_class_name("f4_b").text
        driver.find_element_by_xpath("//div[@class='userMenu']/a[2]/img").click()
        sleep(3)
        check_email = driver.find_element_by_name("email").get_attribute('value')
        check_answerdata = driver.find_element_by_name("passwd_answer").get_attribute('value')
        list1 = [username,email,answerdata]
        check_list1 =[check_username,check_email,check_answerdata]
        sleep(2)
        driver.find_element_by_link_text("退出")
        sleep(2)
        unittest.TestCase.assertEqual(unittest.TestCase(),list1, check_list1, "注册失败")
        return(username,pwd,email,answerdata,phonenumber)