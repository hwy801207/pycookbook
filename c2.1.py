#!/usr/bin/env python3
#-*- encoding:utf-8 -*-
line = 'asdf fjdk; afed, fjek,asdf, foo'
import re

result = re.split(r'[;,\s]\s*', line)
print(len(result))
print(result)
result2 = re.split(r'([;,\s])\s*', line)
print(result2)
