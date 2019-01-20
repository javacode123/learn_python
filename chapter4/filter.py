# -*- coding: utf-8 -*-
# python 内置 filter 函数，filter 也是传递两个参数，一个函数，一个序列，返回的是序列作用于函数返回 True


def is_odd(x):
    return x % 2 == 1


def is_empty(str):
    return str and str.strip()  # 相同为 True


l = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(filter(is_odd, l)))
l = ['a', '', ' ', 'c', '   ']
print(list(filter(is_empty, l)))


# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    s = str(n)
    return s[0:] == s[::-1]


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')