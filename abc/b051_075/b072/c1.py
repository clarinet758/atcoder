#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
a=[int(i) for i in input().split()]
ans=0
d={}
for i in a:
    if i-1 in d:
        d[i-1]+=1
    else:
        d[i-1]=1
    if d[i-1]>ans: ans=d[i-1]
    if i in d:
        d[i]+=1
    else:
        d[i]=1
    if d[i]>ans: ans=d[i]
    if i+1 in d:
        d[i+1]+=1
    else:
        d[i+1]=1
    if d[i+1]>ans: ans=d[i+1]
print(ans)
