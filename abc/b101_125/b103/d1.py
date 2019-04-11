#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import bisect
n,m=map(int,input().split())
w=[]
for i in range(m):
    a,b=map(int,input().split())
    w.append((a,b))
w.sort(reverse=True)
d=[]
for i in range(m):
    a,b=w.pop()
    if i==0:
        d.append([a,b])
    else:
        if d[-1][1]<=a:
            d.append([a,b])
        elif d[-1][1]>b:
            d[-1][1]=b
print(len(d))
