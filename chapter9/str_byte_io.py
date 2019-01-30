# -*- coding: utf-8 -*-
from io import StringIO
from io import BytesIO

# StringIo 在内存中读写 str
f = StringIO()
print(f.write('new line\n'))
print(f.write('second'))

print(f.getvalue())  # 用于获取写入的 str

# 读取 stirngIo
f = StringIO('hello \n i am : kangkang')
for line in f.readlines():
    print(line.strip())

# 二进制操作
f = BytesIO()
f.write('中国'.encode("utf-8"))  # 编码
print(f.getvalue().decode("utf-8"))  # 解码
