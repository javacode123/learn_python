# -*- coding: utf-8 -*-
from collections import Iterable

# 字典遍历
d = {'kangkang': 88, 'michael': 99, 'jane': 88}
for k in d:
    print(k, ':', d[k])
for k, v in d.items():
    print(k, ":", v)

# list 遍历
l = list(range(10))
for i in l:
    print(i)
for c in "abcd":
    print(c)

# 判断一个对象是否可以迭代
print(isinstance([1, 2, 3], Iterable))

# 带下标的循环
for i, value in enumerate('abcdefg'):
    print(i, ':', value)


# 请使用迭代查找一个 list 中最小和最大值，并返回一个 tuple
def find_min_and_max(l):
    if len(l) <= 0:
        return None, None
    min_value = l[0]
    max_value = l[0]
    for value in l:
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value
    return min_value, max_value


if find_min_and_max([]) != (None, None):
    print('测试失败!')
elif find_min_and_max([7]) != (7, 7):
    print('测试失败!')
elif find_min_and_max([7, 1]) != (1, 7):
    print('测试失败!')
elif find_min_and_max([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')




