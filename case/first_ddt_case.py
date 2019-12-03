#conding=utf-8
import ddt
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import time
import HTMLTestRunner
import os
from util.excel_util import ExcelUtil

#拿到excel里的数据
ex = ExcelUtil()
data = ex.get_data()

@ddt.ddt
class FirstDdtCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        image_file_path = os.path.join(os.path.dirname(os.getcwd()) + "/bg-image/register_code.png")
        cls.file_name = image_file_path
        print("所有case的前置")

    @classmethod
    def tearDownClass(cls):
        print("所有case的后置")


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.registerb = RegisterBusiness(self.driver)
        print("执行了当前case的前置条件")

    def tearDown(self):
        time.sleep(5)
        for method, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd() + "/report/" + case_name + ".png")
                self.driver.save_screenshot(file_path)
            else:
                return None
        self.driver.close()
        print("执行了当前case的后置条件")
    '''
    @ddt.data(
        ['gzj@163.com','abc123','111111','file_name','email_error'],
        ['gzj@163.com', 'abc123', '111111', 'file_name', 'name_error'],
        ['gzj@163.com', 'abc123', '111111', 'file_name', 'password_error'],
        ['gzj@163.com', 'abc123', '111111', 'file_name', 'code_error'],
    )
    @ddt.unpack
    def test_register_case(self,email,username,password,code,assertCode):
        email_error = self.registerb.register_function(email,username,password,code,assertCode)
        time.sleep(5)
        self.assertFalse(email_error,'case01-出错了')
    '''
    #结合excel
    @ddt.data(*data)
    def test_register_case(self,data):
        email, username, password, code, assertCode = data
        email_error = self.registerb.register_function(email,username,password,code,assertCode)
        time.sleep(5)
        self.assertFalse(email_error,'case01-出错了')

if __name__ == '__main__':
    test_html_path = os.path.join(os.getcwd()+"\\report"+"\\first_case.html")
    f = open(test_html_path,'wb')
    #执行类First'DdtCase里的所有case
    suite = unittest.TextLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is my 3 report",description="这是我的第3份测试报告",verbosity=2)
    runner.run(suite)