#!/usr/bin/env python3
#-*- encoding:utf-8 -*-

"""
python cookbook 1.1 
"""


"""打印到文件中，而不是标准输出"""
def pr(arg, f):
    print(arg, file=f)
    print(arg)
f2 = open("test2.txt", 'a')

a1 = (1, 2, 3)
a, b, c = a1
print(a);
print(b);
print(c);

"""字符串可迭代"""
str1 = "hello"
a, *_, c = str1
print(a)
print(c)

"""文件对象可迭代"""
f = open("test.txt")
first, *mid, end = f
pr(first, f2)
pr(end, f2)
print("---------------------------")
"""迭代器"""
f = open("test.txt")
itf = iter(f) '''这是个迭代器了'''
first, *mid, end = itf
print(first)
print(mid)
print(end)
print("---------------------------")
'''生成器'''
def nn(n):
    while(n > 0):
        yield n
        n-=1
c = nn(5)
first, *mid, end = c
pr(first, f2)
pr(end, f2)
