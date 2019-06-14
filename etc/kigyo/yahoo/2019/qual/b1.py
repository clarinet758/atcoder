#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

d=[0]*4
for i in range(3):
    a,b=map(int,input().split())
    d[a-1]+=1
    d[b-1]+=1
d.sort()
print(["NO","YES"][d[0]==d[1]==1 and d[2]==d[3]==2])
