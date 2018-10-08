#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,y=map(int,input().split())
for i in range(n+1):
    for j in range(n+1-i):
        tmp=y-(i*10000+j*5000)
        if tmp>=0 and n==i+j+tmp//1000:
            print(i,j,tmp//1000)
            exit()
print("-1 -1 -1")
