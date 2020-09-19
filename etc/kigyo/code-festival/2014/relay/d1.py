#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
l=[input() for i in range(n)]
x=y=0
for i in range(n):
    a=b=""
    for j in range(n):
        if "X" not in a:
            a+=l[j][i]
        if "Y" not in b:
            b+=l[-j-1][i]
    x+=len(a)
    y+=len(b)
print("X" if x>y else "Y" if x<y else "Impossible")
