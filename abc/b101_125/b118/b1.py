#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,m=map(int,input().split())
l=set([i+1 for i in range(m)])
for i in range(n):
    k=[int(j) for j in input().split()]
    t=set([k[j+1] for j in range(k[0])])
    l=l&t
print(len(l))
