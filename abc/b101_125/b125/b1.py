#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
v=[int(i) for i in input().split()]
c=[int(i) for i in input().split()]
ans=0
for i in range(n):
    if v[i]-c[i]>0: ans+=v[i]-c[i]
print(ans)
