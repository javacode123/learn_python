# -*- coding: utf-8 -*-
import os
# 系统信息
print(os.uname())
# 系统
print(os.name)
# 环境变量
print(os.environ)
# 获取当前位置的绝对路径
print(os.path.abspath('.'))
# 使用 os 自带的函数进行路径的分割
print(os.path.split('/Users/zjl/PycharmProjects/python3_learn/chapter9'))
# 使用 os 自带的函数添加路径, 可以根据不同的系统添加不同的文件分割符
print(os.path.join('/Users/zjl/PycharmProjects/python3_learn', 'chapter9'))
# 获取文件扩展名
print(os.path.splitext("/users/zjl/x.ini"))
# 文件重命名
# print(os.rename('io.ini', 'io.txt'))
# 获取当前文件夹下的所有文件名, 过滤掉文件夹
print([x for x in os.listdir('.') if os.path.isfile(x)])
# 获取所有 .py 结尾的文件
print([x for x in os.listdir('.') if os.path.splitext(x)[1]=='.py'])