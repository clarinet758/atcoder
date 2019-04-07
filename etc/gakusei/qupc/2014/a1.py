#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
a,b,c,d=map(int,input().split())
p=[]
for i in range(c):
    l=[int(i) for i in input().split()]
    l.sort(reverse=True)
    p.append(l[b-1])
p.sort(reverse=True)
print(p[d-1])
