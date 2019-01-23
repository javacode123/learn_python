# -*- coding: utf-8 -*-
# python 中的模块，一个 .py 文件就叫做一个模块（Moudle）,对于 py 文件命名不要与系统内置函数重名
# 如果模块名冲突，python 按照目录组织模块，称为包，每个包目录下必须要有一个 __init__.py 文件，不然不会被认为包
import chapter3.slice as slince
from chapter5 import hello_module
# 调用 slice 中的 trim 函数
print(slince.trim("hello "))
hello_module.test()
print(hello_module.__author__)
