#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,m=map(int,input().split())
k=[[int(i) for i in input().split()] for j in range(m)]
p=[int(i) for i in input().split()]
ans=chk=0
for i in range(2**n):
    l=[0]*n
    for j in range(n):
        if i&1: l[j]=1
        i=i>>1
    y=0
    for j in range(m):
        x=0
        for a in range(k[j][0]):
            if l[k[j][a+1]-1]==1: x+=1
        if x%2==p[j]%2: y+=1
    if y==m: ans+=1
print(ans)
