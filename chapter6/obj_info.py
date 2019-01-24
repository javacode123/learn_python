# -*- coding: utf-8 -*-
from chapter6 import Animal


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')


if __name__ == "__main__":
    d = Animal.Dog()
    # --------------- 内置函数解析对象 --------------
    print(isinstance(d, Animal.Animal))  # True
    print(type(d))  # 获取对象信息, type 不会显示父类信息，优先使用 isinstance
    print(isinstance(d, (Animal.Cat, Animal.Animal)))  # 符合 （cat，animal）中的一种就是 True
    print(dir(d))  # 打印 d 的所有属性和方法
    print(hasattr(d, 'run'))  # 是否拥有指定属性
    print(getattr(d, 'run'))  # 获取属性描述