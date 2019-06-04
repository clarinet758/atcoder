#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,m=map(int,input().split())
for i in range(m//n+1,0,-1):
    if m%i==0:
        print(i)
        break

