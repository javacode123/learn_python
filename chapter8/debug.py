# -*- coding: utf-8 -*-
# python 中的 bug 调试
# 使用 print 但是会生成大量的 print 信息，最后还需要删除
# 使用断言：凡是使用 print 的地方都可以使用断言
import logging as log
# logging 配置
log.basicConfig(level=log.INFO)


def foo(x):
    print(">>> x :", x)
    assert x != 0, 'n is zero !'
    return x


def test_log(x):
    if x == 0:
        log.info("x in zero !")
    return x


if __name__ == "__main__":
    # foo(99)
    # foo(0)
    test_log(0)