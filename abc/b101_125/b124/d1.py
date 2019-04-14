#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from collections import deque
n,k=map(int,input().split())
s=input()
f=int(s[0])
d=[0]
if f==0: d.append(0)
t=s[0]
for i in s:
    if i==t:
        d[-1]+=1
    else:
        d.append(1)
        t=i
if s[-1]=="0": d.append(0)
ans=chk=0
for i in range(len(d)):
    chk+=d[i]
    if i>=(2*k+1):
        chk-=d[i-(2*k+1)]
    if i%2==0:
        ans=max(ans,chk)
print(ans)
"""
"""
