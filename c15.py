#!/usr/bin/env python3
#-*- encoding:utf-8 -*-
rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
        ]

from operator import itemgetter
from itertools import groupby

#先sort
rows.sort(key = itemgetter('date'))

#后groupby
for value, items in groupby(rows, key=itemgetter('date')):
    print(value)
    for item in items:
        print(item)


#使用defaultdic完成多value的字典映射

from collections import defaultdict

rows_of_date = defaultdict(list)
for row in rows:
    rows_of_date[row['date']].append(row)


for key, value in rows_of_date.items():
    print(key)
    for v in value:
        print(v)
