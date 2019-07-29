#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,k=map(int,input().split())
a=[int(i) for i in input().split()]
ans=[-1,-1]
for i in range(n):
    if ans[1]<a[i]<k:
        ans[0]=i+1
        ans[1]=a[i]
print(ans[0])
