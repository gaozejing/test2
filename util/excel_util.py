#coding=utf-8

import xlrd
import xlwt
from xlutils3.copy import copy

class ExcelUtil:
    def __init__(self,exce_path=None,index=None):
        #判断excel文件路径和index下标是否为空
        if exce_path == None:
            self.exce_path = "C:\\Users\\高泽静\\PycharmProjects\\test\config\\casedata.xls"
        else:
            self.exce_path = exce_path
        if index == None:
            index = 0
        #打开excel文件
        self.data = xlrd.open_workbook(self.exce_path)
        #获取文件内数据
        self.table = self.data.sheets()[index]

    #获取行数，并进行判断
    def get_lines(self):
        #拿到excel文件写了数据的行数
        rows = self.table.nrows
        #判断文件中是否有数据（也就是行数是否大于等于1）
        if rows >= 1:
            return rows
        return None
    #获取单元格数据，通过单元格所在的行和列定位
    def get_col_value(self,row,cell):
        if row <= self.get_lines():
            data = self.table.cell(row,cell).value
            return data
        return None

    #写入数据，通过xlutils中的copy方法复制原文件数据，再写入
    def write_value(self,row,value):
        if row <= self.get_lines():
            read_value = xlrd.open_workbook(self.exce_path)
            write_data = copy(read_value)
            write_data.get_sheet(0).write(row,9,value)
            write_data.save(self.exce_path)
        else:
            return None
    '''
    #获取一行的数据，并返回所有行list的大list列表
    def get_data(self):
        result = []
        for i in range(self.rows):
            row = self.table.row_values(i)
            result.append(row)
        return result
    '''


if __name__ == '__main__':
    excelutil = ExcelUtil()
    print(excelutil.get_col_value(2,3))
