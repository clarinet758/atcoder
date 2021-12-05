#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
l=[int(i) for i in input().split()]
a=[0,0]
b=[0,0]
t=pow(2,n)
w=t//2
for i in range(t):
    if i>=w:
        if b[0]<l[i]:
            b[0]=l[i]
            b[1]=i
    else:
        if a[0]<l[i]:
            a[0]=l[i]
            a[1]=i
print(a[1]+1 if a[0]<b[0] else b[1]+1)
