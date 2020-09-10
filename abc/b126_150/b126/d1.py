#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import collections
n=int(input())
d=[2]*n
w=collections.deque()
for i in range(n-1):
    a,b,c=map(int,input().split())
    if i==0:
        d[a-1]=0
        d[b-1]=c%2
    elif d[a-1]!=2:
        d[b-1]=(d[a-1]+c%2)%2
    elif d[b-1]!=2:
        d[a-1]=(d[b-1]+c%2)%2
    else:
        w.append((a,b,c))

while len(w):
    a,b,c=w.pop()
    if d[a-1]!=2:
        d[b-1]=(d[a-1]+c%2)%2
    elif d[b-1]!=2:
        d[a-1]=(d[b-1]+c%2)%2
    else:
        w.appendleft((a,b,c))
for i in d:
    print(i)
