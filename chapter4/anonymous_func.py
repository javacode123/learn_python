# -*- coding: utf-8 -*-
# 匿名函数使用  lambda x: x * x 相当于 def f(x): return x * x
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6])))
# 匿名函数也是一个函数对象，可以进行赋值给一个变量，匿名函数可以有效防止函数重名
f = lambda x: x * x
print(f, f(5))


# 测试，构造匿名函数
def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
print(L)
l = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(l == L)
