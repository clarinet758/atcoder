#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

a,b,n=map(int,input().split())
x=input()
for i in x:
    if i=="S" and a>0:
        a-=1
    elif i=="C" and b>0:
        b-=1
    elif i=="E" and ((a==b and a>0) or a>b):
        a-=1
    elif i=="E" and a<b:
        b-=1
print(a)
print(b)
