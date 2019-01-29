# -*- coding: utf-8 -*-
import unittest
from chapter8.MyDict import MyDict


# 测试用例需要继承 unittest.TestCase
class TestDict(unittest.TestCase):

    def setUp(self):
        print('测试方法执行前执行')

    # 测试方法以 test 开头
    def test_init(self):
        d = MyDict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = MyDict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def tests_keye_rror(self):
        d = MyDict()
        with self.assertRaises(KeyError):
            d['empty']

    def tearDown(self):
        print('测试方法执行后执行')


if __name__ == '__main__':
    # 运行单元测试
    unittest.main()
