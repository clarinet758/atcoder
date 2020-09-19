#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
ans=0
for i in range(1,n):
    if i%2: ans+=1
print(1-ans/n)
