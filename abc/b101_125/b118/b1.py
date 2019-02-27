#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,m=map(int,input().split())
for i in range(n):
    k=[int(j) for j in input().split()]
    t=set([k[j+1] for j in range(k[0])])
    if i==0: l={j for j in t}
    else: l=l&t
print(len(l))
