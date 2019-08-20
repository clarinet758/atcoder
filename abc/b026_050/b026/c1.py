#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def sol(v):
    a=1
    b=10*9+7
    for i in d[v]:
        if len(d[i]):
            sol(i)
        a=max(a,w[i])
        b=min(b,w[i])
    if len(d[v])>1: w[v]=a+b+1
    else: w[v]=a*2+1

n=int(input())
d={i:[] for i in range(1,n+1)}
w=[1]*(n+1)
for i in range(n-1):
    p=int(input())
    d[p].append(i+2)
sol(1)

print(w[1])
    
