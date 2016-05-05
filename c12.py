#!/usr/bin/env python3
#-*- encoding:utf-8 -*-

'''
统计次数出现最多的元素
'''

words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
]

from collections import Counter

word_counts = Counter(words)


top_three = word_counts.most_common(3)

#可动态更新
word_counts.update({'cctv':100})

print(top_three)
print (len(word_counts))
