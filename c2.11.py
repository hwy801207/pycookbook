#!/usr/bin/env python3

s = ' hello world \n'
print(s.strip())

print(s.lstrip())
print(s.rstrip())

s = '----hello===='
print(s.strip('-='))
print(s.strip('-'))
