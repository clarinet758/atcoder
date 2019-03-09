#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


n,m=map(int,input().split())
ans=[0]*2
l=[]
for i in range(n):
    a,b=map(int,input().split())
    l.append((a,b))
l.sort()
for i,j in l:
    if ans[1]+j<=m:
        ans[0]+=i*j
        ans[1]+=j
    else:
        ans[0]+=i*(m-ans[1])
        break
print(ans[0])
