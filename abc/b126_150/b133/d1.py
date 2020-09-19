#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
a=[int(i) for i in input().split()]
ans=[0]*n
for i in range(n):
    if i%2: ans[0]-=a[i]
    else: ans[0]+=a[i]

for i in range(1,n):
    ans[i]=(a[i-1]-ans[i-1]//2)*2
print(*ans)
