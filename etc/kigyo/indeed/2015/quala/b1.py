#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import collections
a="indeednow"
b=collections.Counter(a)
n=int(input())
for i in range(n):
    s=input()
    t=collections.Counter(s)
    f=1
    for j in t:
        if j not in b or t[j]!=b[j]:
            f=0
    print(["NO","YES"][f])
        
