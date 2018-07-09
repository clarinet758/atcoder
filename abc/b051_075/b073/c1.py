#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
l=set()
for i in range(n):
    a=int(input())
    if a in l: l.remove(a)
    else: l.add(a)
print(len(l))
