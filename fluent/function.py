# -*- coding: utf-8 -*-
# @Time    : 2019-09-12 15:37
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : function.py
# @Software: PyCharm

"""
装饰器相当于把一个函数替换成另一个函数
"""
registry = []


def register(func):
    print('running register %s' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1')


@register
def f2():
    print('running f2')


def f3():
    print('running f3')


if __name__ == '__main__':
    print(registry)
    f3()
