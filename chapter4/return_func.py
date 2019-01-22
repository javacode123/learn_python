# -*- coding: utf-8 -*-
# 使用函数作为函数的返回值


# 可变参数求和
def calc_sum(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


# 如果不需要立即求和，而是在后面的代码中，根据需要再计算，可以不反回结果，而是返回求和的函数
def lazy_sum(*args):

    def calc_sum():
        sum_values = 0
        for n in args:
            sum_values += n
        return sum_values
    return calc_sum


f1 = lazy_sum(1, 2, 3, 4)
f2 = lazy_sum(1, 2, 3, 4)
# 每次都产生心得函数，即使传入相同的参数
print(f1, f1 == f2, f2() == f1())