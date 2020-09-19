#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

mod=1000000007
n,m,x=map(int,input().split())
w=[]
for i in range(n):
    w.append([int(i) for i in input().split()])
ans=mod
for i in range(2**n):
    d=0
    chk=[0]*m
    for j in range(n):
        if (i>>j&1):
            d+=w[j][0]
            for k in range(m):
                chk[k]+=w[j][k+1]
        
    if min(chk)>=x:
        ans=min(ans,d)
print(ans if ans!=mod else -1)
