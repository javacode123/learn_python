# -*- coding:utf-8 -*-
# python 内置排序函数, sorted 类似一种映射，先把 list 按照函数映射成另一个 list 排序，在根据映射求得原 list

result = sorted([1, 4, 6, 2, 3, 0])
print(result)
# 按照绝对值大小排序 key 是指定的函数作用到 list 上，[-9, -8, 6, 7, 8, 0] -> [9, 8, 6, 7, 8, 0]
# -> [0, 6, 7, 8, 8, 9] -> [0, 6, 7, -8, 8, -9]
print(sorted([-9, -8, 6, 7, 8, 0], key=abs))
# 默认按照字母顺序排序
print(sorted(['b0b', 'cob', 'Alice', 'd', 'M']))
# 忽略大小写排序, 先转换小写，排序，给出排序对应的原字母
print(sorted(['b0b', 'cob', 'Alice', 'd', 'M'], key=str.lower))
# 原序列的基础上，反向排序
print(sorted(['b0b', 'cob', 'Alice', 'd', 'M'], key=str.lower, reverse=True))

# 测试
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    """按照名字排序"""
    return t[0]


def by_score(s):
    return s[1]


L2 = sorted(L, key=by_name)
print(L2)
L2 = sorted(L, key=by_score)
print(L2)
