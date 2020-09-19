#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
a=[int(i) for i in input().split()]
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
ans=0
for i in d:
    ans+=d[i]*(d[i]-1)//2
for i in a:
    print(ans-(d[i]*(d[i]-1))//2+((d[i]-1)*(d[i]-2)//2))
