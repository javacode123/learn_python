# -*- coding: utf-8 -*-
import functools
import time


def log_ex(fun):

    def wrapper(*args, **kwargs):
        print('before execute : %s', fun.__name__)
        return fun(*args, **kwargs)
    return wrapper


def log_high(text):
    def decorator(func):
        def wrapper(*args):
            print("%s %s", text, func.__name__)
            return func(*args)
        return wrapper
    return decorator


# @log_ex
@log_high('execute')
def now():
    return 'zjl'


f = now
# 使用 f(）执行函数
# print(f, f())
# 获取函数名字
# print(f.__name__, now.__name__,)
# 装饰器模式，现在需要再 now 函数调用之前自动打印日志，且不希望修改 now 函数的定义,
# @log_ex 相当于 now = log_ex(now), 执行 now() 相当于执行 log_ex(now)
# print(now())
# 编写需要传入参数的装饰器, 相当于 now = log_high('execute')(now)
print(now(), now.__name__)

# ============== 完整装饰器 ==============


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('%s', func.__name__)
        return func(*args, **kwargs)
    return wrapper


# 带参数的装饰器
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s', func.__name__, text)
            return func(*args, **kwargs)
        return wrapper
    return decorator


# 测试  请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('%s executed in %s ms' % (func.__name__, 10.24))
        return func(*args, **kwargs)
    return wrapper


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
