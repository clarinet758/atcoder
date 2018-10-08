#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n,x=map(int,input().split())
tmp=10000
for i in range(n):
    m=int(input())
    x-=m
    tmp=min(tmp,m)
    
print(x//tmp+n)
