# -*- coding: utf-8 -*-
class Student(object):
    """ object 表示从 object 继承而来 """
    def __init__(self, name, score):  # self 表示实例本身，__init__ 第一个参数永远是 self
        self.name = name
        self.score = score

    def print_score(self):
        """ 类方法 """
        print(self.name, self.score)


if __name__ == '__main__':
    bart = Student('a', 99)
    # 自由的给 bart 绑定属性
    bart.class_no = 90
    print(bart.class_no)
    bart.print_score()
