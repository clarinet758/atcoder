#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,x=map(int,input().split())
s=input()
for i in s:
    x=[max(0,x-1),x+1][i=="o"]
print(x)
