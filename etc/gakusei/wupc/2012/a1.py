#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

p=[0,31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m,d=map(int,input().split())
x,y=map(int,input().split())
ans=-d+y
if m<x: ans+=sum(p[m:x])
print(ans)
