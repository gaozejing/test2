#coding=utf-8
import sys
sys.path.append("C:\\Users\\高泽静\\PycharmProjects\\test")
from util.excel_util import ExcelUtil
from keyword_selenium.actionMethod import ActionMethod

#调用日志1
from log.user_log import UserLog
log = UserLog()
logger = log.get_log()


class KeywordCase(object):


    def run_main(self):
        #调用日志2
        logger.info("kaishi")
        #一般放在大teardown中
        log.close_handle()

        self.action_method = ActionMethod()
        #实例化对象
        handle_excel = ExcelUtil()
        #获取excel文件的行数
        case_lines = handle_excel.get_lines()
        #判断行数是否为空（也就是是否是有数据的文件）
        if case_lines:
            #取每一行的值，这里因为第一行是表头，所以不用取
            for i in range(1,case_lines):
                #取用例的可执行状态的值，这里默认是第三列
                is_run = handle_excel.get_col_value(i,3)
                #根据值判断这个可执行状态
                if is_run == 'yes':
                    #取第4、5、6列，分别为方法名、输入的值、操作的对象
                    method = handle_excel.get_col_value(i,4)
                    send_value = handle_excel.get_col_value(i, 5)
                    handle_value = handle_excel.get_col_value(i, 6)

                    #取第7、8列，分别为获取预期结果的方法、预期结果的值
                    except_method = handle_excel.get_col_value(i,7)
                    except_result = handle_excel.get_col_value(i,8)

                    #执行方法
                    self.run_method(method,send_value,handle_value)

                    #实际结果与预期结果进行对比，并将对比后的结果写到实际结果中
                    #首先判断预期结果的值单元格是否有数据
                    if except_result !='':
                        #如果有数据，则通过（获取结果的值）方法获取到单元格内的数据（list）
                        except_value = self.get_except_value(except_result)
                        #判断列表的第一个数，也就是等号左边的数据
                        if except_value[0] =='text':
                            #如果为test则直接调用方法获取值
                            result = self.run_method(except_method)
                            #将获取的实际的值与预期的等号右边的数据比较
                            if except_value[1] in result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        elif except_value[0]=='element':
                            result = self.run_method(except_result,except_value[1])
                            if result:
                                handle_excel.write_value(i, 'pass')
                            else:
                                handle_excel.write_value(i,'fail')


    #获取预期结果的值(用等号拆分）
    def get_except_value(self,data):
        #返回的是一个列表
        return data.split('=')


    def run_method(self,method,send_value='', handle_value=''):

        #getattr()函数用于返回对象属性值
        #获取ActionMethod()中属性为method的值，这里根据method返回对应的方法
        method_value = getattr(self.action_method,method)
        #判断是否有输入值
        #若有值，执行的是element_sand_keys,只有这个方法需要传2个参数
        if send_value:
            result = method_value(handle_value,send_value)
        else:
            if handle_value:
                result = method_value(handle_value)
            else:
                result = method_value()
        return result

if __name__ == '__main__':
    c = KeywordCase()
    c.run_main()