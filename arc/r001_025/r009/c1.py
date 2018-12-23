#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#bubunnnnn
mod=1777777777
def eof(e): print(e);exit()

def dfs(p,z):
    if p==n:
        if z==0: return 1
        else: return 0
    ret=0
    for i in range(n):
        if u[i]: continue
        u[i]=1
        t=z
        if (i!=p): t-=1
        ret+=dfs(p+1,t)
        u[i]=0
    return ret

n,k=map(int,input().split())
u=[0]*n
if n>8: eof(0)
print(dfs(0,k))

