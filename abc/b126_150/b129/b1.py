#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
w=[int(i) for i in input().split()]
d=[0]*n
for i in range(n):
    d[i]=d[i-1]+w[i]
ans=chk=d[-1]
for i in range(n-1):
    ans=min(ans,abs(d[-1]-d[i]-d[i]))
print(ans)
