#!/usr/bin/env python3
#-*- encoding:utf-8 -*-

a = {'x':1, 'z': 3}
b = {'y':2, 'z': 4}

from collections import ChainMap

c = ChainMap(a, b , {'w': 1})

print(c['x'])
print(c['y'])
print(c['z'])
print(c['w'])
print(len(c))
print(c.get('x'))
c['x'] = 50
print(c.get('x'))
print(a['x'])
print(c)

"""
利用update合并字典
因为会创建新的dict所以不会影响原字典，但是ChainMap会影响原字典
"""
merged = dict(b)
merged.update(a)
print(merged['x'])
print(merged['y'])
print(merged['z'])
print(merged)
