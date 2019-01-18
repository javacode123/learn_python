# -*- coding: utf-8 -*-
""" 切片 """
l = ['kang', 'micahel', 'jane']
# 取前 n 个元素
for i in range(2):
    print(l[i])
# 使用切片
print(l[0:2])
print(l[:2])
print(l[-2:-1])
print(l[-2:])

l2 = list(range(10))
print(l2)
print(l2[0:10:2])  # 每两个取一个
print(l2[::5])  # 每五个取一个

# ======== 练习 ：实现一个trim()函数，去除字符串首尾的空格 ==========
def trim(s):
    if len(s) <= 0 or (s[0] != ' ' and s[-1] != ' '):
        return s
    else:
        if s[0] == ' ':
            s = s[1:]
            return trim(s)
        if s[-1] == ' ':
            s = s[:-1]
            return trim(s)


if trim('hello  ') != 'hello':
    print('1测试失败!')
elif trim('  hello') != 'hello':
    print('2测试失败!')
elif trim('  hello  ') != 'hello':
    print('3测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('4测试失败!')
elif trim('') != '':
    print('5测试失败!')
elif trim('    ') != '':
    print('6测试失败!')
else:
    print('测试成功!')