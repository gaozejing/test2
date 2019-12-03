#coding=utf-8
from selenium import webdriver
import time
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest

#最好把实例化放在最外面
driver = webdriver.Chrome()

#初始化方法
def driver_init():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    time.sleep(5)

#获取element信息方法
def get_element(id):
    element = driver.find_element_by_id(id)
    return element

#获取随机的8位字符串
def get_range_user():
    user_info = ''.join(random.sample('1234567890asdfghjkl',8))
    return user_info

#获取验证码图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_id("getcode_num")
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width'] + left
    height = code_element.size['height'] + top
    # 打开原截图，并通过坐标截取验证码区域图片，并保存
    im = Image.open(file_name)
    img = im.crop((left, top, right, height))
    #验证码的图片直接替换掉页面的图片
    img.save(file_name)

#解析图片获取验证码
def code_online(file_name):
    # 读取图片中的字符串
    r = ShowapiRequest("http://route.showapi.com/1274-2", "119070", "5183ccbb187e48bab5cea7d8c977b13c")
    r.addFilePara("imgFile", file_name)
    res = r.post()
    # 取json里的值
    text = res.json()['showapi_res_body']['texts']
    return text

#运行主程序
def run_main():
    user_name_info = get_range_user()
    user_email = user_name_info+"@163.com"
    file_name = "C:/Users/高泽静/PycharmProjects/test/bg_img/test01.png"

    driver_init()
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(user_name_info)
    get_element("register_password").send_keys("111111")
    get_code_image(file_name)
    text = code_online(file_name)
    get_element("captcha_code").send_keys(text)
    get_element("register-btn").click()
    driver.close()

run_main()