# -*- coding: utf-8 -*-
# python 内置字典，在其他语言中叫做 map, 使用键值存储, 具备快速查找的功能, list [], dict {}
d = {"michael": 95, "kangkang": 80, "jane": 99}
d.pop("jane")  # 删除键值对
d["jane"] = 100  # 添加
print(d)

contain = "kangkang" in d  # 判断 key 是否存在字典中
if contain:
    print(d.get("kangkang"))

# 遍历
for key in d:
    print(key, ':', d[key])

for k, v in d.items():
    print(k, ':', v)

# 集合 set, 集合里面的元素不能重复,
s = set([1, 2, 3, 2])
s.add(1)
s.add(4)
print(s)
s.remove(4)  # 移除指定元素
print(s)

