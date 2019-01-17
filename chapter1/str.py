# -*- coding: utf-8 -*-
# utf-8 可变编码，char 一个字节，汉字三个字节， unicode 统一编码，全部占用相同的自己，
# ascii 只有一个字节
print('汉语')  #使用 unicode 编码
print(ord('汉'))  # 打印单个字符的 unicode 编码
print(chr(27721))  # 将编码转换为字符
y = '中文'
x = b'abc'  # 每个字符占用一个字节
y.encode("utf-8")  # 转换编码格式
print(y)

# 格式化
s = "hello:%s, 我是周杰伦，我欠你%f元 %%" % ('zjl', 10.0)
print(s)