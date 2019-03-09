#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,m,c=map(int,input().split())
b=[int(i) for i in input().split()]
ans=0
for i in range(n):
    a=[int(i) for i in input().split()]
    chk=c
    for  j in range(m):
       chk+=b[j]*a[j]
    if chk>0: ans+=1
print(ans)
