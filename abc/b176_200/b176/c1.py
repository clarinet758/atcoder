#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
a=[int(i) for i in input().split()]
x=min(a)
for i in range(n):
    a[i]-=x
ans=chk=0
chk=a[0]
for i in range(n):
    if a[i]<chk:
        ans+=chk-a[i]
    else:
        chk=a[i]
print(ans)
