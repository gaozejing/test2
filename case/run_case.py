#coding=utf-8
import unittest
import os

class RunCase(unittest.TestCase):
    def test_case01(self):
        #获取当前工程目录
        case_path = os.path.join(os.getcwd(),'')

        #discover三个参数（路径，匹配规则，第三个可不填）
        #匹配规则是py文件名称
        suite = unittest.defaultTestLoader.discover(case_path,'unittest_*.py')

        unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()