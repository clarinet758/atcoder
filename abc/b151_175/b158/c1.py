#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

a,b=map(int,input().split())
for i in range(13,10001):
    x=i*100+i*8
    y=i*100+i*10
    x//=100
    y//=100
    if (x==i+a and y==i+b):
        print(i)
        exit()
print(-1)
