#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n,m=map(int,raw_input().split())
d={i:[i] for i in range(1,n+1)}
for i in range(m):
    u,v=map(int,raw_input().split())
    d[u].append(v)
    d[v].append(u)
ans=1
for i in range(1<<n):
    tmp=[]
    for j in range(n):
        if i&1:
            tmp.append(j+1)
        i=i>>1
    f=1
    for j in tmp:
        if len(set(tmp)&set(d[j]))!=len(tmp):
            f=0
            break
    if f==1:
        ans=max(ans,len(tmp))
print ans
