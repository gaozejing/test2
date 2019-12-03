#coding=utf-8
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import time
import HTMLTestRunner
import os

class FirstCase(unittest.TestCase):

    #所有case的前置条件
    @classmethod
    def setUpClass(cls):
        #保存验证码截图的路径（最好用相对路径，绝对路径当换一个环境就不一定正确了）
        image_file_path = os.path.join(os.path.dirname(os.getcwd())+"/bg-image/register_code.png")
        #因为下面几乎每个函数都要用到，所以写在前置函数里方便使用
        #前置函数就类似于构造函数
        cls.file_name = image_file_path
        print("所有case的前置")

    #所有case的后置条件
    @classmethod
    def tearDownClass(cls):
        print("所有case的后置")

    #每个case的前置条件
    #前置放driver，就不需要构造方法了
    #每执行一次case都需要重启浏览器
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.registerb = RegisterBusiness(self.driver)
        print("执行了当前case的前置条件")

    #每个case的后置条件
    #后置，每执行一次case都需关闭浏览器
    def tearDown(self):
        time.sleep(5)
        #拿到报错信息（有则显示报错信息，无则为None，._outcome.errors返回的是个列表
        for method,error in self._outcome.errors:
            #如果有报错信息
            if error:
                #先拿到报错时的用例名称
                case_name = self._testMethodName
                #文件路径，以case函数名称命名（一定要注意/是否有遗漏）
                file_path = os.path.join(os.getcwd()+"/report/"+case_name+".png")
                #截图报错时的页面，并保存
                self.driver.save_screenshot(file_path)
            else:
                return None
        self.driver.close()
        print("执行了当前case的后置条件")

    #错误邮箱用例
    def test_login_email_error(self):
        email_error = self.registerb.register_email_error('gzj@163.com','abc123','111111',self.file_name)
        time.sleep(5)
        #assert函数的使用，相当于用if语句进行判断
        self.assertFalse(email_error,'case01-出错了')
        #下面和上面作用相似，但用assert更简洁
        '''
        if email_error == True:
            print("case01-错误邮箱执行失败")
        else:
            print("case01-错误邮箱执行成功")
        '''
    #错误用户名用例
    def test_login_username_error(self):
        username_error = self.registerb.register_username_error('@111','11','111111',self.file_name)
        time.sleep(5)
        self.assertFalse(username_error,'case02-出错了')

    #错误密码用例
    def test_password_error(self):
        password_error = self.registerb.register_password_error('@111','abc123','1',self.file_name)
        time.sleep(5)
        self.assertFalse(password_error,'case03-出错了')

    #错误验证码用例
    def test_login_code_error(self):
        code_error = self.registerb.register_code_error('@111','abc123','111111',self.file_name)
        time.sleep(5)
        self.assertFalse(code_error,'case04-出错了')

    #字段均正确，注册成功用例
    def test_login_success(self):
        success = self.registerb.register_success('123@111.com','abcffffff23','111111',self.file_name)
        time.sleep(5)
        self.assertTrue(success,'case05-出错了')


if __name__ == '__main__':
    #获取测试报告.html文件的路径
    test_html_path = os.path.join(os.getcwd()+"\\report"+"\\first_case.html")
    #打开文件并获得文件流
    f = open(test_html_path,'wb')


    #执行所有case
    #unittest.main()

    #执行其中一条case
    suite= unittest.TestSuite()
    #suite.addTest(FirstCase('test_login_email_error'))
    #suite.addTest(FirstCase('test_login_username_error'))
    #suite.addTest(FirstCase('test_password_error'))
    #suite.addTest(FirstCase('test_login_code_error'))
    suite.addTest(FirstCase('test_login_success'))
    #测试的过程中将日志、结果等信息写进文件流里面
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is my first report",description="这是我的第二份测试报告",verbosity=2)
    runner.run(suite)
    #unittest.TextTestRunner().run(suite)