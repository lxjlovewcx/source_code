import unittest
from selenium import webdriver
from time import time
from time import sleep
from random import randint, choice
import os
from selenium.webdriver.support.select import Select
class TestFriendlyLink(unittest.TestCase):  
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.base_url="http://172.31.31.100:8200/"
        #设置元素超时时间
        self.driver.implicitly_wait(10)
        #页面加载超时时间
        self.driver.set_page_load_timeout(10)
        #异步脚本加载的超时时间
        self.driver.set_script_timeout(10)
        #窗口最大化
        self.driver.maximize_window()
        self.path=os.path.dirname(os.getcwd())
        
    
    def test_01(self):
        for i in range(1):
            driver=self.driver 
            driver.get(self.base_url)
            email_a="1450732536@qq.com"
            password_a="123456"
            actural_name1="李龙"
            email_b="851677798@qq.com"
            password_b="123456"   
            actural_name2="李雪健"  
            email_c="87654321@qq.com"
            password_c="123456"   
            actural_name3="李飞"   
            accrig_list=['凭密码访问']
    # 3品论权限：任何人可评论，好友可评论，关闭评论
            comrig_list=["任何人可评论","好友可评论","关闭评论"]
            
#     print()
            for accrig in accrig_list:
                for comrig in comrig_list:
                    self.Logincll(driver,email_a,password_a,actural_name1)
                    src,picture,content=self.Login123(driver,accrig,comrig)
                    self.checkblog_acss(driver,email_b,password_b,actural_name2,content,accrig,comrig,src,picture,friend=True)
                    self.checkblog_acss(driver,email_c,password_c,actural_name3,content,accrig,comrig,src,picture,friend=False)
    def Logincll(self,driver,email,password,actural_name):    
        driver.find_element_by_name("email").send_keys(email)
        driver.find_element_by_name("passwd").send_keys(password)
        driver.find_element_by_name("button").click()
        name1=driver.find_element_by_id("my_name").text
        self.assertEqual(actural_name, name1)
    
    def Login123(self,driver,accrig,comrig):
        #         1 点击链接发表 发表
        content=accrig+"+"+comrig+str(time())
        driver.find_element_by_link_text("发表").click()
        # 2 权限：任何人可见，仅好友可见，私密日记，凭密码访问，默认选择任何人可见
        
        # 4：输入标题：id=title点位，输入内容为任何人可见+任何人课评论+str（time（））
        driver.find_element_by_name("title").send_keys(content)
        # 5：在输入框中输入文本类容：切换到这个frame，class=ke-iframe，在定位到class=ke-content
        iframe_element=driver.find_element_by_class_name("ke-iframe")
        driver.switch_to_frame(iframe_element)
        sleep(1)
        driver.find_element_by_class_name("ke-content").send_keys(content)
        
        # 6:输入文本水几岁。
        
        # 7：切换回来默认页面，使用xpath，title=插入笑脸，//a[@title=插入笑脸]
        driver.switch_to_default_content()
        sleep(1)
        driver.find_element_by_xpath("//a[@title='插入笑脸']").click()
        sleep(1)
        # 8:定位到class=ke-menu的div，返回所有的img标签，，并随机选择一个
        img_list=driver.find_element_by_class_name("ke-menu").find_elements_by_tag_name("img")
#         print(img_list)
        img=choice(img_list)
        src=img.get_attribute("src")
        img.click()
        sleep(1)
        # 9：插入图片，首先是链接编辑：
        picture="timg"+str(randint(0,9))+".jpg"
        path1=self.path+"\\denglu\图片\\"+picture
#         print(path1)
        print(path1)
        sleep(1)
        # 当前路径-7+“图片/”+"timg0.jpg"
        # 10: id=ajax_upload_attach_process,shuru 9
        driver.find_element_by_name("myfile").send_keys(path1)
        sleep(1)
        # 11:
    #         选择下拉菜单权限访问
        access_=driver.find_element_by_name("privacy")
#         print(access_)
        sel1=Select(access_)
        sel1.select_by_visible_text(accrig)
    #         选择下拉菜单评论权限
        if "凭密码访问"==accrig:
            driver.find_element_by_name("password").send_keys("123456")
        conment_=driver.find_element_by_id("cc")
        sel2=Select(conment_)
        sel2.select_by_visible_text(comrig)
        driver.find_element_by_xpath("//input[@value='发 表']").click()
        sleep(2)
        self.Check_blog_info(driver,content,src,picture)
    #         好友登录
        driver.find_element_by_link_text("退出").click()
        return src,picture,content
    
    def Check_blog_info(self,driver,content,src,picture):
        actural_title=driver.find_element_by_class_name("tit_log").find_element_by_tag_name("strong").text
        actural_content=driver.find_element_by_id("blog_con").text
        actural_src=driver.find_element_by_id("blog_con").find_element_by_tag_name("img").get_attribute("src")
        actural_picture=driver.find_element_by_class_name("adjunct_list").find_element_by_class_name("cGray2").text
        self.assertEqual(content, actural_title)
        self.assertEqual(content, actural_content)
        self.assertEqual(src, actural_src)
        self.assertEqual(picture, actural_picture) 
    
    def checkblog_acss(self,driver,email,password,actural_name,content,accrig,comrig,src,picture,friend=False):
                # 登录指定的账号
        
        self.Logincll(driver,email,password,actural_name)
        
        # 点击随便看看
        driver.find_element_by_link_text("随便看看").click()
                # 点击指定的日志
        driver.find_element_by_link_text(content).click()
        # 如果访问权限是'任何人可见',
        if "任何人可见"==accrig :  
        # 检查日志  class=tit_log/h1/strong.text    id=blog_con.text    id=blog_con  tag img get arr
        #src
            self.Check_blog_info(driver,content,src,picture) 
            self.check_cc(driver,comrig,content,actural_name,friend)
        elif "仅好友可见"==accrig :
            if friend:
                self.Check_blog_info(driver,content,src,picture)
                self.check_cc(driver,comrig,content,actural_name)
            else:
                self.check_privacy_tip(driver,"只有主人的好友可以查看此日志")
        # 如果访问权限是'仅好友可见'
        # 如果是好友：检查日志
        # 如果不是好药：检查提示信息
        # 如果访问权限是','私密日记''
        elif "私密日记"==accrig :
        # 检查提示信息
        # 如果访问权限是''凭密码访问'
            self.check_privacy_tip(driver,"只有主人可以查看此日志")
        else:  
        # 1判断是否出现提示信息
            try: 
                self.check_privacy_tip(driver,"本日志需要密码才能访问 ")
                driver.find_element_by_name("password").send_keys("123456")    
            # 2输入密码
            # 3：点击提交根据class btn_b
                driver.find_element_by_class_name("btn_b").click()
                
            except:
                print("出异常了，不能弹出密码输入框")
            self.Check_blog_info(driver,content,src,picture)
            self.check_cc(driver,comrig,content,actural_name,friend)
        # 4：陌生人可访问日志，查看日志
        # 5：好友可访问日志，查看日志
    
        # 检查评论权限
        driver.find_element_by_link_text("退出").click()
    def check_cc(self,driver,comrig,content,actural_name,friend=True):
        if '任何人可评论'==comrig:
            self.check_blog_comment(driver,content,actural_name)
        # 
        # 如果评论权限为任何人可评论：
        # 添加新品论并检查评论是否成功
        elif '好友可评论'==comrig:
            if friend:
                self.check_blog_comment(driver,content,actural_name)
            else:
                print(content,actural_name)
                self.check_cc_tip(driver,"您无法评论,日志发布者设置好友可评论")       
        # 如果权限为好友可评论：
        # 如果是好友，则：添加新品论并检查评论是否成功
        # 如果不是好友，则：检查提示信息
        else:
            self.check_cc_tip(driver,"您无法评论,日志发布者已经关闭评论")
        # 如果权限为关闭评论，：
        # 检查提示信息
        # 
        # 添加新评论
        # 输入框随机输入内容 textarea
        # 先定位出所有的评论记录li标签class comlist 并取出第一个
        # 通过上级li标签，遭到下一级的作者名字//h3[@class=''tit_critique]/a
        # 通过上级li标签，找到下级的评论内容 tag p
    def check_blog_comment(self,driver,content,actural_name):
        driver.find_element_by_name("textarea").send_keys(content)
        driver.find_element_by_id("content_submit").click()
        a=driver.find_elements_by_class_name("comlist")
        actural_content=a[0].find_element_by_tag_name("p").text
        print(content,actural_content)
        self.assertEqual(content, actural_content)
        actural_namex=a[0].find_element_by_xpath("//h3[@class='tit_Critique lh25 mb5']/a").text
        self.assertEqual(actural_name, actural_namex)
    def check_privacy_tip(self,driver,tip):
        actural_tip=driver.find_element_by_class_name("bg_msg").text
        self.assertIn(tip, actural_tip)
    
    def check_cc_tip(self,driver,msg):
        tip=driver.find_element_by_class_name("LogList").text
        self.assertIn(msg, tip)
    def tearDown(self):
        self.driver.quit()
          
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
