#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# pscl 要修正
n=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
ans=chk=sum(a)+b[-1]
for i in range(-1,-n,-1):
    chk=chk-a[i]+b[i-1]
    ans=max(ans,chk)
print(ans)
