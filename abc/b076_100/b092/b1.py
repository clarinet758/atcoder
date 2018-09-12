#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
d,x=map(int,input().split())
for i in range(n):
    a=int(input())
    x+=d//a+[1,0][d%a==0]
print(x)
