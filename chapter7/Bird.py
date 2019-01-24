# -*- coding: utf-8 -*-
# 在 python 中 __value 表示私有属性， __solts__ 声明属性范围，__init__() 表示构造方法
# 总之 __vlaue__ 都有自己的作用


class Bird(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "this is %s" % self.name


print(Bird("xiao_niao"))  # <__main__.Bird object at 0x10ba19470>
print(Bird("xiao_niao").__str__())  # 两种方式等价

