#coding=utf-8
import sys
sys.path.append('C:\\Users\\高泽静\\PycharmProjects\\test')
from selenium import webdriver
import time
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest
from base.find_element import FindElement

class RegisterFunction(object):
    #创建构造函数
    def __init__(self,url,i):
        self.driver = self.get_driver(url,i)
    #获取driver并且打开url
    def get_driver(self,url,i):
        if i==1:
            driver = webdriver.Chrome()
        elif i==2:
            driver = webdriver.Firefox()
        driver.get(url)
        driver.maximize_window()
        return driver
    #获取定位
    def elementfind(self,key):
        #实例化对象是靠构造函数创建的
        getelement = FindElement(self.driver)
        element = getelement.find_element(key)
        return element
    #元素中输入信息
    def send_user_info(self,key,data):
        self.elementfind(key).send_keys(data)

    #获取随机数
    def get_range_user(self):
        user_info = ''.join(random.sample('1234567890asdfghjkl', 8))
        return user_info

    # 获取验证码图片
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.elementfind('code_image')
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        # 打开原截图，并通过坐标截取验证码区域图片，并保存
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        # 验证码的图片直接替换掉页面的图片
        img.save(file_name)

    # 解析图片获取验证码
    def code_online(self,file_name):
        # 读取图片中的字符串
        r = ShowapiRequest("http://route.showapi.com/1274-2", "119070", "5183ccbb187e48bab5cea7d8c977b13c")
        r.addFilePara("imgFile", file_name)
        res = r.post()
        # 取json里的值
        text = res.json()['showapi_res_body']['texts']
        return text


    def run_main(self):
        user_name_info = self.get_range_user()
        user_email = user_name_info + "@163.com"
        file_name = "C:/Users/高泽静/PycharmProjects/test/bg_img/test01.png"
        text = self.code_online(file_name)

        self.send_user_info('user_email',user_email)
        self.send_user_info('user_name', user_name_info)
        self.send_user_info('password',"111111")
        self.get_code_image(file_name)
        self.send_user_info('code_text',"111111")
        self.elementfind('btn').click()
        code_error = self.elementfind('code_text_error')
        if code_error == None:
            print("注册成功")
        else:
            self.driver.save_screenshot("C:/Users/高泽静/PycharmProjects/test/bg_img/test02.png")
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    for i in range(1,3):
        register_function = RegisterFunction('http://www.5itest.cn/register',i)
        register_function.run_main()