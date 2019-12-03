#coding=utf-8
import configparser
class ReadIni(object):
    #构造函数
    #默认文件路径为空
    #若路径为空，则使用默认路径
    def __init__(self,file_name=None,node=None):
        if file_name == None:
            file_name = "C:\\Users\\高泽静\\PycharmProjects\\test\\config\\LocalElement.ini"
        if node ==None:
            self.node ="LoginElement"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)
    #加载ini文件
    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf
    #获取值
    def get_value(self,key):
        data = self.cf.get(self.node, key)
        return data
