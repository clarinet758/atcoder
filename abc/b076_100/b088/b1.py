#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# pscl 要修正
n=int(input())
l=[int(i) for i in input().split()]
ans=sum(l)
l.sort()
for i in range(-2,-n-1,-2):
    ans-=l[i]*2
print(ans)
