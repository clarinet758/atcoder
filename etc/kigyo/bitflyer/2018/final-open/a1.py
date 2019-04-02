#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

d=[10]
for i in range(10):
    d.append(d[-1]*10)
ans=12
n=int(input())
for i in range(n):
    q=int(input())
    for j in range(11):
        if q%d[j]:
            ans=min(ans,j)
print(ans)
