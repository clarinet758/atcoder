#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bisect import bisect_left
input()
a=[int(i) for i in input().split()]
d=[a[0]]
for i in a[1:]:
    if i>d[-1]: d.append(i)
    else: d[bisect_left(d,i)]=i
print(len(d))
