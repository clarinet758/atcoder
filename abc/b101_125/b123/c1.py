#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
d=[]
ans=0
for i in range(5):
    x=int(input())
    d.append(x)
print(5+(n-1)//min(d))
