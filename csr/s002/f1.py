#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
d=set()
for i in range(n):
    a,b=map(int,input().split())
    d.add((min(a,b),max(a,b)))
print(len(d))
