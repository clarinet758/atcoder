#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
a=[int(i) for i in input().split()]
s=[0]
for i in range(n):
    s.append(s[-1]+a[i])
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
ans=chk=0
for i in d:
    ans+=(d[i]*(d[i]-1))//2
print(ans)
