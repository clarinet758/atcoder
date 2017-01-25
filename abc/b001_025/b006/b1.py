#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n=int(raw_input())
l=[0]*(4)
l[3]=1

for i in range(4,10**6+1):
    l.append(((l[i-1]+l[i-2])%10007+l[-3])%10007)
print l[n]
