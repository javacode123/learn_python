# -*- coding: utf-8 -*-
class Animal(object):
    def run(self):
        print('animal run ...')


class Dog(Animal):
    def run(self):
        print('dog run ...')

    def bar(self):
        pass


class Cat(Animal):
    pass


if __name__ == "__main__":
    # Dog Cat 继承 Animal, 可以获得父类全部功能
    Animal().run()
    d = Dog()
    d.run()
    # --------------- 内置函数解析对象 --------------
    print(isinstance(d, Animal))  # True
    Cat().run()
    print(type(d))  # 获取对象信息, type 不会显示父类信息，优先使用 isinstance
    print(isinstance(d, (Cat, Animal)))  # 符合 （cat，animal）中的一种就是 True
    print(dir(d))  # 打印 d 的所有属性和方法
    print(dir(str))
    print(hasattr(d, 'run'))  # 是否拥有指定属性
    print(getattr(d, 'run'))  # 获取属性描述
