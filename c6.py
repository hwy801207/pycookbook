#!/usr/bin/env python3

from collections import defaultdict

d = defaultdict(list)

d['a'].append(1);
d['a'].append(2);
d['a'].append(2);
d['b'].append(4);

print(d)
print("-"*20)
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['a'].add(2)
d['b'].add(4)
print(d)
d = defaultdict(list)
d['a']
print("-"*20)
print(d)
