#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n,a,b=[int(i) for i in input().split()]
x=[int(i) for i in input().split()]
ans=chk=0
for i in range(1,n):
    ans+=min(b,(x[i]-x[i-1])*a)
print(ans)
