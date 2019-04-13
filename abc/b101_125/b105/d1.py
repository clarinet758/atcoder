#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,m=map(int,input().split())
l=[int(i) for i in input().split()]
ans=t=0
d={0:1}
for i in l:
    t=(t+i)%m
    if t in d: d[t]+=1
    else: d[t]=1
for i in d:
    ans+=d[i]*(d[i]-1)
print(ans//2)
