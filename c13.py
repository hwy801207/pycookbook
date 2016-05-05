#!/usr/bin/env python3
#-*- encoding:utf-8 -*-
'''
字典列表排序
库强大,但是质量不高
'''
rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
        ]


from operator import itemgetter

sorted_by_fname = sorted(rows, key=itemgetter('fname', 'lname'))
sorted_by_uid = sorted(rows, key=itemgetter('uid'))
print(sorted_by_uid)
print(sorted_by_fname)



