#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
d={}
for i in range(n):
    w=list(input())
    w.sort()
    s="".join(w)
    if s in d:
        d[s]+=1
    else:
        d[s]=1
ans=0
for i in d:
    ans+=d[i]*(d[i]-1)//2
print(ans)
