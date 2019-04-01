#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#TLE!!!

n,q=map(int,input().split())
s=input()
r=[1]*n
w={}
for i,j in enumerate(s):
    if j in w:
        w[j].append(i)
    else:
        w[j]=[i]
for i in w:
    w[i].sort()
for i in range(q):
    t,d=map(str,input().split())
    if t not in w: continue
    if d=="L":
        for j in w[t]:
            if j>0:
                r[j-1]+=r[j]
            r[j]=0
    else:
        for j in w[t][::-1]:
            if j<n-1:
                r[j+1]+=r[j]
            r[j]=0
print(sum(r))
