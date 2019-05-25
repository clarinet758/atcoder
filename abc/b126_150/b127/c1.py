#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


n,m=map(int,input().split())
d=[1,n]
for i in range(m):
    l,r=map(int,input().split())
    d[0]=max(d[0],l)
    d[1]=min(d[1],r)
print(max(0,(d[1]-d[0]+1)))

"""

3-6

4-5

2-8
5-9

"""
