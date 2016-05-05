#!/usr/bin/env python3
#-*- encoding:utf-8 -*-
"""
切片命名

"""

record = '....................100 .......513.25 ..........'

SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
print("cost = ", cost)

a = slice(2, 10, 1)
print("a.start", a.start)
print("a.start", a.stop)
print("a.start", a.step)

s = "hellooooooworld"
a.indices(len(s))
print(s[a])

