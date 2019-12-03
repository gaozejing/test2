#coding=utf-8
import unittest

class FirstCase01(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self):
        print(self._outcome.errors)
        for method,error in self._outcome.errors:
            if error:
                print("errorrrrrrr")
        print("执行了后置条件")
    def testfirstcase(self):
        a = False
        self.assertTrue(a)
        print(a)
    def testf(self):
        print("222")

if __name__ == '__main__':
    unittest.main()