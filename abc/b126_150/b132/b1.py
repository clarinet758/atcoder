#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
p=[int(i) for i in input().split()]
ans=0
for i in range(2,n):
    chk=[p[i-2],p[i-1],p[i]]
    chk.sort()
    if chk[1]==p[i-1]:
        ans+=1
print(ans)
