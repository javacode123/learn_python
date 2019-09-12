# -*- coding: utf-8 -*-
# @Time    : 2019-09-12 13:34
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : encode.py
# @Software: PyCharm
"""
文件存储：文本在计算机中是用字节存储的，所以必须吧文子按照不同编码转换成字节流存储，
不同编码相当于不同的映射表，把文件映射成字节，读取的时候使用不同的解码方式解码。
"""

if __name__ == '__main__':
    city = 'الأضحى'
    s = city.encode('utf-16')  # 编码成字节序列
    print(s.decode('utf-16'))  # 解码
    print(type(5))
