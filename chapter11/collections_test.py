# -*- coding: utf-8 -*-
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter, ChainMap
# python 集合类

# namedtuple 创建一个 tuple 子类, 可以指定属性
Point = namedtuple('Point', ['x', 'y'])
point_a = Point(4, 5)
print(point_a)
print(isinstance(point_a, Point), isinstance(point_a, tuple))
# namedtuple('名称', 属性[])
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# 双向表 deque
q = deque(['a', 'b', 'c'])
q.append('d')  # 从末尾插入
q.appendleft('0')  # 从头插入
q.insert(0, '-1')  # 从头插入
print(q.pop(), q.popleft())  # 末尾出元素, 首部出元素

# defaultdict 在 dict 中如果 key 不存在会抛出 keyError, 通过 defaultdict 当 key 不存在返回默认值
default_dict = defaultdict(lambda: 'N/A')  # 默认值通过调用函数返回
default_dict['key'] = 'value'
print(default_dict['key'], default_dict['no_exit'])

# OrderedDict 排序字典，按照添加顺序排列
d = OrderedDict({'a': 9, 'c': 10, 'b': 11})
d['d'] = 11
print(d.keys())
for key, value in d.items():
    print(key, value)

# Counter 计数器，相当于一个 dict
c = Counter()
for i in "abcddcbs":
    c[i] = c[i] + 1
print(c, dict(c)['a'])

# ChainMap 把一组 dict 串起来形成逻辑上的 dict
d1 = {'key1': 8, 'key2': 9}
d2 = {'key3': 10}
# 将 d1 d2 串起来, 查找 cm[key] 依次从 d1[key] d2[key] 查找, 如果存在就返回
cm = ChainMap(d1, d2)
print(cm['key3'], cm)
