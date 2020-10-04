#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,k=map(int,input().split())
a=[int(i) for i in input().split()]
w=[1]
x=set([1])
for i in range(k):
    t=a[w[-1]-1]
    if t in x: break
    x.add(t)
    w.append(t)
p=w.index(t)
k-=p
loop=len(w)-p
print(w[p+k%loop])
