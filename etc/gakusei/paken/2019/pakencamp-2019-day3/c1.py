#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,m=map(int,input().split())
a=[[int(i) for i in input().split()] for j in range(n)]
ans=chk=0
for i in range(m-1):
    for j in range(i+1,m):
        chk=0
        for k in range(n):
            chk+=max(a[k][i],a[k][j])
        ans=max(ans,chk)
print(ans)
