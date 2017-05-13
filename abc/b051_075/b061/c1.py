#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n,k=map(int,input().split())
d={}
l=[]
for i in range(n):
    u,v=map(int,input().split())
    if u in d:
        d[u]+=v
    else:
        d[u]=v
        l.append(u)
l.sort()
for i in l:
    k-=d[i]
    if k<=0:
        print(i)
        break
