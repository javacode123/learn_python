# -*- coding: utf-8 -*-
# python 异常处理
import logging as log


def divid(x, y):
    try:
        print('try ...')
        r = x / y
        print('result', r)
    except ZeroDivisionError as e:
        print('except', e)
        # raise ValueError('ERROR !')
    except ValueError as e:  # 多个异常
        print('except', e)
    else:  # 没有异常会执行此段代码
        print('no except')
    finally:  # 不管有没有异常都执行 finally
        print('finally ...')
    print('end ...')


# ========== 测试 ========
from functools import reduce


def str2num(s):
    try:
        int(s)
        return int(s)
    except ValueError as e:
        print("value error", e)
        return float(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

if __name__ == "__main__":
    divid(4, 0)
    divid(5, 2)
    main()
    # if True:
    #  raise ValueError('test error')  # 抛出错误

