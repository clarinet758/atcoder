#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
a=[int(i) for i in input().split()]
chk=a[0]
ans=l=r=0
while 1:
    if chk==n: ans+=1
    if chk<=n and r<n-1:
        r+=1
        chk+=a[r]
    elif chk>n:
        chk-=a[l]
        l+=1
    else:
        break
print(ans)
