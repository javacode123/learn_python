# -*- coding: utf-8 -*-
def my_abs(x):
    if not isinstance(x, (float, int)):
        raise TypeError("bad opteration")
    if x >= 0:
        return x
    else:
        return -x


def complex_value(x, y):
    """ 返回多个值 """
    return x, y


def nop():
    """ 空函数 """
    pass  # pass 语句什么都不做，可以用来做站位符，例如没有写好如何实现，可以先放一个 pass


print(my_abs(-3) == 3)
print(complex_value(5, 6))
# print(my_abs("ii"))
nop()
