#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
h=[int(i) for i in input().split()]
ans=chk=1
t=h[0]
for i in range(1,n):
    if h[i]<=t:
        chk+=1
        ans=max(ans,chk)
    else:
        chk=1
    t=h[i]
print(ans-1)
