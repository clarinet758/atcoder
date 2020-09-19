#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
input=sys.stdin.readline
n=int(input())
h=[int(i) for i in input().split()]
t=h[0]-1
for i in range(1,n):
    if t>h[i]:
        print("No")
        exit()
    elif t<h[i]:
        h[i]-=1
    t=h[i]
    
print("Yes")
