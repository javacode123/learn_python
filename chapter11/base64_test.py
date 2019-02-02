# -*- coding: utf-8 -*-
import base64

# 使用 base64 来表示任意的二进制数据, base64 是一种常用的二进制编码方式
"""
    编码原理：
        首先准备 64 个不同的字符用于编码, 将二进制数据每 6bit 表示一组，
        则可以表示 2~6 个字符，每组表示的数值映射到 64 为字符组, 如果数据流
        最后不够一组则使用 \x00 追加，编码之后使用 = , 一个 = 表示凑一个字符
"""
print(base64.b64encode(b'zjl3016'))  # b'str' 存储时把 str 转为bytes, r'str' 非转义
print(base64.b64decode(base64.b64encode(b'zjl3016')))
