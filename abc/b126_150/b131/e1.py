#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,k=map(int,input().split())
d=[]
t=(n-1)*(n-2)//2
if t<k:
    print(-1)
    exit()
for i in range(2,n+1):
    d.append((1,i))
t-=k
for i in range(2,n):
    if t==0: break
    for j in range(i+1,n+1):
        d.append((i,j))
        t-=1
        if t==0: break
print(len(d))
for i in d:
    print(i[0],i[1])
