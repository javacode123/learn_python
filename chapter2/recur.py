# -*- coding: utf-8 -*-


def fact(n):
    """ 递归函数 """
    if n == 1:
        return n
    else:
        return n * fact(n-1)


print(fact(100))