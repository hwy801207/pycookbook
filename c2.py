#!/usr/bin/env python3

"""
cookbook 1.2
"""
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

def avg(grades):
    return sum(grades)//len(grades)

grades = (10, 30, 35, 78, 96)

avg_grade = drop_first_last(grades)
#字符串与数字无法直接拼接
print("平均成绩"+str(avg_grade))
print("原始平均成绩"+str(avg(grades)))

"""
复杂的数据结构
"""

records = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4)
        ]

for tag, *args in records:
    if tag == 'foo':
        print("recoreds is", *args)


"""
忽略某些数据
"""
record = ("ACME", 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print("name", name)
print("year", year)
print("_", _)
