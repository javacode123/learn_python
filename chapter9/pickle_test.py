# -*- coding: utf-8 -*-
import pickle
import json
from chapter9.Student import Student

# python 的运行时的对象都是存在内存中的，有时需要将其存入文件中，一遍直接将对象读入内存
d = {'a': 1, 'b': 2}
f = open('pickle.txt', 'wb')
# 将 dict 写入文件
pickle.dump(d, f)
f.close()

# 加载序列化的对象
with open('pickle.txt', 'rb') as f:
    d = pickle.load(f)
print(d)

# 按照 json 格式存储
d = json.dumps(d)
print(json.dumps([1, 2, 3, 4]))
d = json.loads(d)
print(d)


# 序列化对象 Student
def stu_to_dict(self):
    return {'name': self.name, 'age': self.age}


def dict_to_stu(d):
    return Student(d['name'], d['age'])


s = Student('zjl', 18)

# 使用 pickle 不需要编写序列化方法
str = pickle.dumps(s)
s = pickle.loads(str)
print(s, s.name)

# 编写序列化方法保证对象可以被序列化
str = json.dumps(s, default=stu_to_dict)
print(str)
# 编写解析方法
s = json.loads(str, object_hook=dict_to_stu)
print(s, s.name)

