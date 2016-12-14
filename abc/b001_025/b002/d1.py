#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n,m=map(int,raw_input().split())
d=[[0]*n for i in range(n)]
ans=chk=1
for i in range(m):
    x,y=map(int,raw_input().split())
    d[x-1][y-1]=1
    d[y-1][x-1]=1
for i in range(1<<n):
    w=[]
    for j in range(n):
        if (i>>j&1):
            w.append(j)
    chk=1
    f=0
    for x in w:
        for y in w:
            if x!=y and d[x][y]==0:
                f=1
                break
        if f:
            break
    if f==0:
        ans=max(ans,len(w))

print ans
