# -*- coding: utf-8 -*-
# python 内置函数
print(abs(-1))
# 函数赋值，变量可以指向一个函数
f = abs
print(f(-1))
# 既然变量可以指向一个函数，函数的参数能接受变量，那么一个函数就可以接收另一个函数作为参数，
# 这种函数叫做高阶函数


def add(x, y, fun):
    """ 简单的高阶 fun 是传递的函数 """
    return fun(x) + fun(y)


print(add(-1, -2, abs))
