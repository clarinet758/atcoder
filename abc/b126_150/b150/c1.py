#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import itertools

n=int(input())
p=[int(i) for i in input().split()]
q=[int(i) for i in input().split()]
t=[int(i) for i in range(1,n+1)]
a=b=0
for i,j in enumerate(list(itertools.permutations(t,n))):
    w=[1,1]
    for x,y in enumerate(j):
        if p[x]!=y: w[0]=0
        if q[x]!=y: w[1]=0
    if w[0]: a=i
    if w[1]: b=i

print(abs(a-b))
