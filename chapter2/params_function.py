# -* coding: utf-8 -*-
"""
python 定义函数中有必选参数，默认参数，可变参数，关键字参数，命名参数，且 5 种参数可以组合使用
       参数定义顺序：必选参数，默认参数，可变参数，命名关键字参数，关键字参数
"""


def power(x):
    return x*x


def power(x, n=2):
    """
    x 的 n 次方, 默认参数 2
    默认参数的设置：
        必选参数在前，默认参数在后
        当函数有多个参数时，变化大的参数放在前面，变化小的参数放在后面
    """
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s


def add_end(l=[]):
    """ 重复使用默认参数调用函数，会重复追加 """
    l.append("end")
    return l


print(add_end())
print(add_end())  # 会在上次默认参数的基础上继续调用


def add_end(l=None):
    """ 默认参数必须指向不可变对象 """
    if l is None:
        l = []
    l.append("End")
    return l


def calc_one(numbers):
    """ 固定参数： [1, 2, 3]  (1, 2, 3)"""
    s = 0
    for number in numbers:
        s = s + number
    return s


def calc(*numbers):
    """ 可变参数：1, 2, 3"""
    s = 0
    for number in numbers:
        s = s + number
    return s


def person(name, age, **kw):
    """
    关键字参数：
        可变参数 *args 会把传入的参数封装成 tuple
        关键字参数 **args 会把传入参数封装成 dict
    """
    if 'study' in kw:  # 对 study 直接返回
        return
    print('name:', name, 'age:', age, 'others:', kw)


def person_one(name, age, *, city, study='high'):
    """ 命名关键字参数: 对 * 后的参数进行检查, 只接收 city 关键字 """
    print(name, age, city, study)


print(add_end())
print(add_end())  # 修改之后的函数，默认参数使用不可变对象
print(power(5, 3))
# 旧的函数无法调用，缺乏参数, 使用 power(x, n=2) 可以调用，n 默认值为 2
print(power(5))

print('=========== 可变参数 ===========')
# 可变参数调用
print(calc(1, 2, 3))
numbers = [1, 2, 3]
# 使用 * 号转化为可变参数
print(calc(*numbers))

print('=========== 关键字参数 ===========')
person('kangkang', 35)
person('jane', 44, sex='f', city='bj', study='high')
dict_params = {'sex': 'm', 'city': 'nj'}
person('zjl', 44, **dict_params)
person_one('zjl', 88, city="nj")

print("============ 练习 ==============")


def product(*numbers):
    s = 1
    for n in numbers:
        s = s * n
    return s


print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')


