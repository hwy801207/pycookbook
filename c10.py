#!/usr/bin/env python
#-*- encoding:utf-8 -*-
a = [1,5,2,1,9,1,5, 10]

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

print(list(dedupe(a)))
