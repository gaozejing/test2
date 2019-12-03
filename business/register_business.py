#coding=utf-8
from handle.register_handle import RegisterHandle

class RegisterBusiness(object):
    def __init__(self,driver):
        self.registerh = RegisterHandle(driver)

    #把对元素的操作封装
    def register_base(self,email,username,password,file_name):
        self.registerh.send_email(email)
        self.registerh.send_username(username)
        self.registerh.send_password(password)
        self.registerh.send_code(file_name)
        self.registerh.click_register_button()
        self.registerh.get_register_text()

    #判断是否注册成功
    def register_success(self,email, username, password,file_name):
        self.register_base(email, username, password,file_name)
        if self.registerh.get_register_text() == None:
            return True
        else:
            return False

    #根据传入的assertCode（email_error、name_error、password_error、code_error），来判断是否会出现报错信息，若出现，则返回False
    def register_function(self,email,username,password,code,assertCode):
        self.register_base(email,username,password,code)
        if self.registerh.get_user_text(assertCode)==None:
            return True
        else:
            return False

    '''
    使用数据驱动方法时，以下代码均可省略
    '''
    '''
    #判断邮箱是否输入正确
    def register_email_error(self,email,username,password,file_name):
        self.register_base(email,username,password,file_name)
        if self.registerh.get_user_text('email_error')==None:
            print(self.registerh.get_user_text('email_error'))
            return True
        else:
            print(self.registerh.get_user_text('email_error'))
            return False
        


    #判断用户名是否输入正确
    def register_username_error(self,email,username,password,file_name):
        self.register_base(email, username, password, file_name)
        if self.registerh.get_user_text('name_error')==None:
            print(self.registerh.get_user_text('name_error'))
            return True
        else:
            print(self.registerh.get_user_text('name_error'))
            return False

    #判断密码是否输入正确
    def register_password_error(self, email, username, password, file_name):
        self.register_base(email, username, password, file_name)
        if self.registerh.get_user_text('password_error')==None:
            print(self.registerh.get_user_text('password_error'))
            return True
        else:
            print(self.registerh.get_user_text('password_error'))
            return False

    #判断验证码是否输入正确
    def register_code_error(self, email, username, password, file_name):
        self.register_base(email, username, password, file_name)
        if self.registerh.get_user_text('code_error')==None:
            print(self.registerh.get_user_text('code_error'))
            return True
        else:
            print(self.registerh.get_user_text('code_error'))
            return False
    '''
