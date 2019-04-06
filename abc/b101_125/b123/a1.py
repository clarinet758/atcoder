#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

d=[]
for i in range(5):
    a=int(input())
    d.append(a)
k=int(input())
print("Yay!" if k>=d[-1]-d[0] else ":(")
