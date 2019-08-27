#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bisect import bisect_left

n=int(input())
c=[int(input()) for i in range(n)]
w=[c[0]]
for i in range(1,n):
    if w[-1]<c[i]:
        w.append(c[i])
    else:
        w[bisect_left(w,c[i])]=c[i]
print(n-len(w))
