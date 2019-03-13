#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
l=[int(i) for i in input().split()]
ans=l[0]
for i in range(1,n):
    if l[i]>l[i-1]:
        ans+=(l[i]-l[i-1])
print(ans)
