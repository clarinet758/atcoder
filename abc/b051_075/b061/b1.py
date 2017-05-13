#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n,m=map(int,input().split())
d={i:0 for i in range(1,n+1)}
for i in range(m):
    u,v=map(int,input().split())
    d[u]+=1
    d[v]+=1
for i in range(1,n+1):
    print(d[i])
