#!/usr/bin/env python
#-*- encoding:utf-8 -*-
"""
获取两个字典的相同的值，或者键
利用集合的交 差,但是values不适合，无法保证唯一性
"""

a = {
        'x': 1,
        'y': 2,
        'z': 3
        }
b = {
        'w': 10,
        'x': 11,
        'y': 2
        }
print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())
