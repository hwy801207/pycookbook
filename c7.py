#!/usr/bin/env python
#-*- encoding:utf-8 -*-
from collections import OrderedDict
"""
保持字典的插入顺序，大数据量需要仔细考虑
"""
def ordered_dict():
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['cctv'] = 6

    for key in d:
        print(key, d[key])

ordered_dict()
