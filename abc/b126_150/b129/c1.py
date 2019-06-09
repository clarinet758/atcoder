#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

mod=1000000007
n,m=map(int,input().split())
d=set([])
w=[0]*(n+2)

for i in range(m):
    a=int(input())
    d.add(a)
for i in range(n):
    if i==0 and 1 not in d:
        w[1]=1
    elif i==0 and 1 in d:
        w[1]=0
    if i==0 and 2 not in d:
        w[2]=1
    elif i==0 and 2 in d:
        w[2]=0
    if i>0:
        if i+1 not in d:
            w[i+1]=(w[i+1]+w[i])%mod
        if i+2 not in d:
            w[i+2]=w[i]
print(w[-2]%mod)
