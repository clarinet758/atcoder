#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,x=map(str,input().split())
for i in range(2,11):
    y=0
    for j,k in enumerate(x[::-1]):
        y+=int(k)*(i**j)
    if str(y)==n:
        print(i)
        exit()
        
