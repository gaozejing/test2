#coding=utf-8

from selenium import webdriver
import time
from PIL import Image
from ShowapiRequest import ShowapiRequest

#打开网页
driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
time.sleep(5)
#保存页面截图
driver.save_screenshot("C:/Users/高泽静/PycharmProjects/test/bg_img/imooc.png")
#定位到验证码元素，并获取验证码各个点坐标
code_element = driver.find_element_by_id("getcode_num")
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
#打开原截图，并通过坐标截取验证码区域图片，并保存
im = Image.open("C:/Users/高泽静/PycharmProjects/test/bg_img/imooc.png")
img = im.crop((left,top,right,height))
img.save("C:/Users/高泽静/PycharmProjects/test/bg_img/imooc1.png")
#读取图片中的字符串
r = ShowapiRequest("http://route.showapi.com/1274-2","119070","5183ccbb187e48bab5cea7d8c977b13c" )
r.addFilePara("imgFile", "C:/Users/高泽静/PycharmProjects/test/bg_img/imooc1.png")
res = r.post()
#取json里的值
text = res.json()['showapi_res_body']['texts']
print(text) # 返回信息
#输入验证码
time.sleep(5)
driver.find_element_by_id("captcha_code").send_keys(text)

time.sleep(10)
driver.close()