# -*- coding: utf-8 -*-
class Student:
    __slots__ = ('name', 'age')  # 使用 __slots__ 限制动态绑定实例属性，仅对当前实例有用，继承的无限制

    def get_age(self):
        print(self.age)


class GraduateStudent(Student):
    pass


s = Student()
s.age = 99
# 动态绑定属性
s.name = 'zjl'
s.get_age()
print(s.name)
# s.sex = 'f' 报错，由于 __slots__ 中限制了属性
gs = GraduateStudent()
gs.sex = 'f'  # __slots__ 仅对当前实例有限制作用，对子类无限制作用

