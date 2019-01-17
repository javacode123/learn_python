# -*- coding -*-
# 使用缩进表示 {}
age = 20
if age > 18:
    print("age is", age)
else:
    print("age is not 18")

x = 0  # 非零表示 True
if x:
    print(True)
else:
    print(False)

names = ['kangkang', 'jane', 'michel']
for name in names:
    print(name)

# 从 0 到 9
for i in range(10):
    print("range:", i)
print(list(range(10)))  # range 转化为 list

n = 10
# n == 0 判定为 False
while n:
    print(n)
    n -= 1
