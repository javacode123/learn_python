# -*- coding: utf-8 -*-
# @Time    : 2019-09-12 17:11
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : nolocal.py
# @Software: PyCharm


def average():
    l = []

    def helper(value):
        l.append(value)  # l 并没有赋值，只是 append
        return sum(l) / len(l)

    return helper


def high_average():
    count = 0
    l_sum = 0

    def helper(value):
        nonlocal count, l_sum  # count, l_sum 是赋值操作
        count += 1
        l_sum += value
        return l_sum / count

    return helper


avg = average()
avg(5)
print(avg(6))
