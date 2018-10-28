#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,x=map(int,input().split())
l=[int(i) for i in input().split()]
ans=0
for i in range(1,n):
    if l[i]+l[i-1]>x:
        tmp=l[i]+l[i-1]-x
        ans+=tmp
        l[i]=max(0,l[i]-tmp)
print(ans)
