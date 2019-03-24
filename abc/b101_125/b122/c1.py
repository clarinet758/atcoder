#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,q=map(int,input().split())
s=input()
d=[0]*n
#l=[int(i) for i in input().split()]
for i in range(1,n):
    if s[i-1]=="A" and s[i]=="C":
        d[i]+=d[i-1]+1
    else:
        d[i]=d[i-1]
#print(*d)
for i in range(q):
    l,r=map(int,input().split())
#    print(l,r,s[l-1:r],d[l-1],d[r-1])
    print(d[r-1]-d[l-1])
