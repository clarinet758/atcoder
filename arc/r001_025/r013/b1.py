#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
x=y=z=0
for i in range(n):
    l=[int(i) for i in input().split()]
    l.sort()
    x=max(x,l[0])
    y=max(y,l[1])
    z=max(z,l[2])
print(x*y*z)
