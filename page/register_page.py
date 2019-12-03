#coding=utf-8
from base.find_element import FindElement

class RegisterPage(object):
    def __init__(self,driver):
        self.registerbase = FindElement(driver)

    #获取邮箱输入框元素
    def find_email_element(self):
        return self.registerbase.find_element('user_email')

    #获取用户名输入框元素
    def find_username_element(self):
        return self.registerbase.find_element('user_name')

    #获取密码输入框元素
    def find_password_element(self):
        return self.registerbase.find_element('password')

    #获取验证码输入框元素
    def find_code_text_element(self):
        return self.registerbase.find_element('code_text')

    #获取验证码图片元素
    def find_code_image_element(self):
        return self.registerbase.find_element('code_image')

    #获取注册按钮元素
    def find_register_btn_element(self):
        return self.registerbase.find_element('btn')

    #获取邮箱报错元素
    def find_email_error_element(self):
        return self.registerbase.find_element('user_email_error')

    #获取用户名报错元素
    def find_username_error_element(self):
        return self.registerbase.find_element('user_name_error')

    #获取密码报错元素
    def find_password_error_element(self):
        return self.registerbase.find_element('user_password_error')

    #获取验证码报错元素
    def find_code_error_element(self):
        return self.registerbase.find_element('code_text_error')