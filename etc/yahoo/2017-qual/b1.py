#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n,k=map(int,input().split())
a=[int(i) for i in input().split()]
a.sort()
chk=a[:k]
t=0
if k>1:
    t=k*((k-1)//2)+[0,(k)//2][(k+1)%2]
print(sum(chk)+t)
