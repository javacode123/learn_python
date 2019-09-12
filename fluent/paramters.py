# -*- coding: utf-8 -*-
# @Time    : 2019-09-12 16:35
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : paramters.py
# @Software: PyCharm
b = 9


def f(a):
    print(a)
    print(b)
    # b = 7


if __name__ == '__main__':
    import dis
    print(dis.dis(f))  # 查看字节码，加入 b = 7 后，b是从局部变量拿去，不加 b = 7， b 是从全局变量拿取
