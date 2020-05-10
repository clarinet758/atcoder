#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,k=map(int,input().split())
a=[int(i) for i in input().split()]
d=[0]
w=set([0])
x=0
for i in range(n):
    if a[x]-1 not in w:
        d.append(a[x]-1)
        w.add(a[x]-1)
        x=a[x]-1
    else:
        f=a[x]-1
        break

if k<len(d):
    print(d[k]+1)
else:
    x=k-len(d)
    y=d.index(f)
    z=len(d)-y
    print(d[y+x%z]+1)
