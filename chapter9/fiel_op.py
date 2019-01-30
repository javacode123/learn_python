# -*- coding: utf-8 -*-
import os

# 使用 with 自动调用 f.close()
with open("io.txt", 'r', encoding='UTF-8') as f:
    print(f.read())  # read(）依次读取全部内容

# 写文件，通过调用 f.close() 将存在缓冲区的内容写入磁盘
with open('io.txt', 'w') as f:
    f.write('第四行')  # 模式 w 直接覆盖文件内容， 模式 a 原文件末尾追加

with open("io.txt", 'r', encoding='UTF-8') as f:
    for line in f.readlines():
        print(line.strip())  # strip 去除 '\n'

with open('io.ini', 'r') as f:
    print(f.read())

print("==========================")
if __name__ == "__main__":
    # 当前路径
    print(os.path.abspath('.'))
    # 当前模块
    print(__file__)
