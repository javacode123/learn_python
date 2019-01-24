# -*- coding: utf-8 -*-
class Animal(object):
    __slots__ = ('__name', '__age')  # 限制属性

    def __init__(self, name, age):
        self.__age = age
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        print(self.__age)


# 对于一个完整的类，设置属性应该使用方法设置，方便对设置参数进行检查
a = Animal('zj', 18)
a.get_age()
# print(a.__name) 无法调用
# a.sex = 'f' 无法添加属性


# ============ 上面的调用方法略显复杂 ==============
class Dog(Animal):  # 继承父类构造方法

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, value):
        if not isinstance(value, str):
            raise ValueError("sex must be str")
        self.__sex = 'f'

    @property
    def father(self):
        return self.__sex


d = Dog('a', 99)
d.get_age()
# d.sex = 0 参数检查
d.sex = 'm'
print(d.sex)
print(d.father)
# d.father = 'm' father 属性只读


# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):  # width, height 私有可以设置, resolution 私有，只读

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def resolution(self):
        return self.width * self.height


if __name__ == '__main__':
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)
    if s.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')