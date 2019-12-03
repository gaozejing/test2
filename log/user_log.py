#coding=utf-8
import logging
import os
import datetime

class UserLog():
    def __init__(self):

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.logger.setLevel(logging.INFO)

        #输出日志到控制台
        #consle = logging.StreamHandler()
        #self.logger.addHandler(consle)

        #输出日志到文件
        #用当前日期命名文件
        #拿到当前文件的绝对路径的目录名
        bath_dir = os.path.dirname(os.path.abspath(__file__))
        #日志的目录
        log_dir = os.path.join(bath_dir,"logs")
        #当前时间文件名
        log_file = datetime.datetime.now().strftime("%Y-%m-%d")+".log"
        #完整路径+名字
        log_name = log_dir + "\\" + log_file
        #print(log_name)

        self.file_handle = logging.FileHandler(log_name,'a',encoding='utf-8')
        #logger.addHandler(file_handle)

        #设置日志输出的格式
        formatter = logging.Formatter('%(asctime)s ----->%(filename)s %(funcName)s : %(lineno)d %(levelname)s------->%(message)s ')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)


        #self.logger.debug("test")
        #self.consle.close()
        #以下移除不能放在构造函数里，会在还没写入的时候就关掉了
        #self.logger.removeHandler(file_handle)
        #file_handle.close()

    def get_log(self):
        return self.logger

    #关注性能，不关闭会耗内存
    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()

if __name__ == '__main__':
    log = UserLog()
    log.get_log().debug("ttttt")
    log.close_handle()