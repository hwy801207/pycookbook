#!/usr/bin/env python
#-*- encoding:utf-8 -*-
"""
对字典求最大最小值
zip 返回的是个迭代器无法重复利用
"""

prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
        }

min_price = min(zip(prices.values(), prices.keys()))
print("min value", min_price)
max_price = max(zip(prices.values(), prices.keys()))
print("max value", max_price)
