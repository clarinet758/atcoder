#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n,m,x=map(int,input().split())
a=[int(i) for i in input().split()]
ans=chk=0
for i in a:
    if i<x: ans+=1
    else: chk+=1
print(min(ans,chk))
