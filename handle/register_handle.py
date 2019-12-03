#coding=utf-8
from page.register_page import RegisterPage
from util.get_code import GetCode

class RegisterHandle(object):
    def __init__(self,driver):
        self.registerp = RegisterPage(driver)
        self.registerg = GetCode(driver)

    #在邮箱输入框内输入邮箱
    def send_email(self,email):
        self.registerp.find_email_element().send_keys(email)

    #在用户名输入框内输入用户名
    def send_username(self,username):
        self.registerp.find_username_element().send_keys(username)

    #在密码输入框内输入密码
    def send_password(self,password):
        self.registerp.find_password_element().send_keys(password)

    #在验证码输入框内输入验证码
    def send_code(self,file_name):
        text = self.registerg.code_online(file_name)
        self.registerp.find_code_text_element().send_keys(text)

    #获取报错的文字信息
    def get_user_text(self,info):
        #添加容错处理
        try:
            if info == 'email_error':
                test = self.registerp.find_email_error_element().text
            elif info == 'name_error':
                test = self.registerp.find_username_error_element().text
            elif info == 'password_error':
                test = self.registerp.find_password_error_element().text
            elif info == 'code_error':
                test = self.registerp.find_code_error_element().text
        except:
            test = None
        return test

    #点击注册按钮
    def click_register_button(self):
        self.registerp.find_register_btn_element().click()

    #获取注册按钮的文字
    def get_register_text(self):
        return self.registerp.find_register_btn_element().text
