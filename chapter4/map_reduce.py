# -*- coding: utf-8 -*-
# python 内建 map() 和 reduce() 函数
from functools import reduce


def f(x):
    return x * x


def converse(x):
    x = str(x)
    r = []
    r.append(x[0].upper())
    r.append([i.lower() for i in x[1: -1]])
    return r


def add(x, y):
    return x + y


def change(x, y):
    return x * 10 + y


# 将一个 [1, 2, 3] 转化成 [1, 4, 9], 传入两个参数，一个函数，一个 Iterable,
# 结果作为 Iterator 返回, map 并行计算 Iterable 内容
r = map(f, [1, 2, 3])
print(list(r))
r = map(converse, [1, 2, 3])
print(list(r))

# reduce 函数：把函数结果和 Iterable 的下一个元素做累积运算, 因此传递的函数要有两个参数
# reduce(add, [1, 2, 3]) = add(add(1, 2), 3)
r = reduce(add, [1, 2, 3])
print(r)
print(sum([1, 2, 3]))
# 把序列 [1, 3, 5, 7, 9] 变成整数 13579
print(reduce(change, [1, 3, 5, 7, 9]))


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']


def normalize(x):
    x = str(x)
    r = x[0].upper()
    for c in x[1:]:
        r = r + c.lower()
    return r


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，
# 可以接受一个list并利用reduce()求积
def prod(l):
    def f(a, b):
        return a * b
    return reduce(f, l)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(str):
    l = str.replace(".", "")  # 去除 .

    def fn(x, y):  # 转换整数
        return x * 10 + y

    def fn1(c):  # 字符转数字
        return DIGITS[c]
    return reduce(fn, map(fn1, l))


def str2float(str):
    i = str2int(str)
    return i / 10 ** (len(str) - str.index('.') - 1)


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')





