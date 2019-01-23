# -*- coding: utf-8 -*-

""" 一个标准的 module 模板，第一行表示编码，第二行表示注释，第三行作者，后面开始真正的代码 """

__author__ = "zjl"

import sys


def test():
    args = sys.argv
    print(args)


# 如果文件直接在此文件中运行则 __name__ == "__main__"，如果是其他 module 调用则 __name__ != "__main__"
if __name__ == "__main__":
    test()
