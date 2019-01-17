# -*- coding: utf-8 -*-
'''
    list 是 python 的一种数据类型，是一种有序集合，可以随时添加和删除元素
'''
classmates = ['micahel', 'kangkang', 'jane']
print(classmates, len(classmates), '\n', classmates[0])
print(classmates[-1], classmates[-2])  # 索引最后一个元素
classmates.append('marari')  # 追加
print(classmates)
classmates.pop()  # 删除末尾元素, pop(i) 删除指定索引元素
classmates[-1] = 'a'  # 赋值, 打破排序性
print(classmates)
classmates.append(True)  # 支持不同类型
print(classmates)
lis = [1, 2, 3]
classmates.append(lis)  # 嵌套
print(classmates[4][1])

list1 = [1, 2, 3]
list2 = [4, 5, 6]
for l1, l2 in zip(list1, list2):
    print(l1, l2)
