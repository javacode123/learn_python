# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

# 获取当前时间
now = datetime.now()
print(now, type(now))  # datetime 是模块, 模块内部有一个 datetime 类
# 获取指定日期的时间
ft = datetime(2018, 9, 9, 15)
print(ft)  # 调用的是 datetime 类的 __str__() 方法

# 转换时间戳 1970.01.01 为基准，之后为正，之前为负，且与时区没有关系
print('datetime to timestamp', ft.timestamp())
ts = ft.timestamp()

# 时间戳转化到日期
print('local timestamp to datetime', datetime.fromtimestamp(ts))  # 本地时间
print('utc timestamp to datetime', datetime.utcfromtimestamp(ts))  # utc 时间，标准时间

# str 转为 datetime
print('str to datetime', datetime.strptime("2019-02-01 16:01:20", "%Y-%m-%d %H:%M:%S"))
# datetime 转为 str
print('datetime to str', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# 时间加减，需要导入 timedelta
now_time = datetime.now()
print(now_time, 'add one hour', now_time + timedelta(hours=1))