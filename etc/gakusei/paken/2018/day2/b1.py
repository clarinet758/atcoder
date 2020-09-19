#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,d=map(int,input().split())
a=[int(i) for i in input().split()]
a.sort(reverse=True)
ans=0
for i in range(d-1,n,d):
    ans+=a[i]
print(ans)
