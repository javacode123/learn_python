# -*- coding: utf-8 -*-
import os
# 列表生成
l = list(range(1, 10))
print(l)

# 生成 1*1 2*2 3*3
l = [x * x for x in range(1, 10)]
print(l)
# 生成偶数的平方
l = [x * x for x in range(1, 10) if x % 2 == 0]
print(l)

# 生成全排列
l = [m + n for m in 'abc' for n in 'xyz']
print(l)

# 生成文件夹列表
l = [d for d in os.listdir('.')]
print(l)

# 测试
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [word.lower() for word in L1 if isinstance(word, str)]
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')