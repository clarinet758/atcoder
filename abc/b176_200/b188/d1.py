#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,x=map(int,input().split())
d={}
vv=[]
for i in range(n):
    a,b,c=map(int,input().split())
    if a in d:
        d[a]+=c
    else:
        d[a]=c
        vv.append(a)
    if b+1 in d:
        d[b+1]-=c
    else:
        d[b+1]=-c
        vv.append(b+1)

ans=chk=0
vv.sort()
p=len(vv)
for i in range(p-1):
    di=vv[i+1]-vv[i]
    chk+=d[vv[i]]
    if chk<x:
        ans+=chk*di
    else:
        ans+=x*di
print(ans)
