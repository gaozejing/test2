#coding=utf-8

from selenium import webdriver
from base.find_element import FindElement
import time

class ActionMethod(object):

    def __init__(self):
        pass

    #打开浏览器方法,传入浏览器类型
    #仅支持（chrome、firefox、edge、ie）
    def open_browser(self,browser):
        if browser == 'Chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'Edge':
            self.driver = webdriver.Edge()
        elif browser == 'IE':
            self.driver = webdriver.Ie()
        else:
            print("暂不支持该浏览器")

    #输入地址方法，传入地址
    def get_url(self,url):
        if url != None:
            self.driver.get(url)
        else:
            print("请输入地址")

    #定位元素
    def get_element(self,key):
        find_element_ = FindElement(self.driver)
        element = find_element_.find_element(key)
        return element

    #输入元素
    def element_send_keys(self,key,value):
        element = self.get_element(key)
        element.send_keys(value)

    #点击元素
    def element_click(self,key):
        element = self.get_element(key)
        element.click()

    #等待时间
    def sleep_time(self,value):
        time.sleep(value)

    #关闭浏览器
    def close_browser(self):
        self.driver.close()

    #获取页面title
    def get_title(self):
        return self.driver.title