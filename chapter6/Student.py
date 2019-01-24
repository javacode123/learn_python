# -*- coding: utf-8 -*-
class Student(object):
    """ object 表示从 object 继承而来 """
    def __init__(self, name, score):  # self 表示实例本身，__init__ 第一个参数永远是 self
        self.__name = name  # 私有变量不可以被外部访问，obj.__name 无法访问, 只能在类内部访问
        self.__score = score  # __name:表示私有变量，__name__:表示特殊变量

    def print_score(self):
        """ 类方法 """
        print(self.__name, self.__score)


class Student_entend:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender


if __name__ == '__main__':
    bart = Student('a', 99)
    # 自由的给 bart 绑定属性
    bart.class_no = 90
    print(bart.class_no)
    bart.print_score()
    # print(bart.__name)
    bart = Student_entend('Bart', 'male')
    if bart.get_gender() != 'male':
        print('测试失败!')
    else:
        bart.set_gender('female')
        if bart.get_gender() != 'female':
            print('测试失败!')
        else:
            print('测试成功!')
