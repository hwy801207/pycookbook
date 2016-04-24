#!/usr/bin/env python
#-*- encoding:utf-8 -*-
"""
slice() 制造切片

"""

items = [0, 6, 5, 4, 3, 12]
a = slice(2, 4)
b = items[a]
print(b)
print("b.start()", a.start)
print("b.stop()", a.stop)
