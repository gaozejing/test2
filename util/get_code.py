#coding=utf-8
import sys
sys.path.append('C:\\Users\\高泽静\\PycharmProjects\\test')
from PIL import Image
from ShowapiRequest import ShowapiRequest
from base.find_element import FindElement
from page.register_page import RegisterPage

class GetCode(object):
    def __init__(self,driver):
        self.driver = RegisterPage(driver)

    # 获取验证码图片
    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_code_image_element()
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
    def code_online(self, file_name):
        # 读取图片中的字符串
        r = ShowapiRequest("http://route.showapi.com/1274-2", "119070", "5183ccbb187e48bab5cea7d8c977b13c")
        r.addFilePara("imgFile", file_name)
        res = r.post()
        # 取json里的值
        text = res.json()['showapi_res_body']['texts']
        return text