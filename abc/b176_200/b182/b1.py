#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
a=[int(i) for i in input().split()]
ans=chk=0
for i in range(2,1001):
    x=[j for j in a if j%i==0]
    if len(x)>chk: ans,chk=i,len(x)
print(ans)
