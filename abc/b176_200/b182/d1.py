#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
a=[int(i) for i in input().split()]
p=[0]*(n+1)
for i in range(n):
    p[i+1]=p[i]+a[i]
ans=now=chk=m=r=0
for i in p:
    m=max(m,i)
    ans=max(ans,now+m)
    now=now+i
print(ans)
