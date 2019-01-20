# -*- coding: utf-8 -*-
# 生成器：在列表生成式中会直接生成一个完整的列表，有时可能只需要访问列表的前几项，
# 可以通过生成器记录生成公式，边计算边生成，不需要直接生成

l = (i for i in range(10))
print(l)  # 输出的是一个生成器对象
print(next(l))
print(next(l))
# 也可以通过 for 迭代
for i in l:
    print(i)


# 斐波拉切数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1
    return 'done'


# 生成式表达
def fib_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 保存生成记录，用来记录计算到了哪里
        a, b = b, a+b
        n = n + 1
    return 'done'


# 通过 next() 函数获取 yeeld 的值
print(next(fib_generator(6)))


def triangles():
    L = [1]
    while True:
        yield L
        S = L[:]
        S.append(0)
        L = [S[i-1]+S[i] for i in range(len(S))]


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
