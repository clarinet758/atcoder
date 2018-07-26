#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n,k=map(int,input().split())
a=[int(i) for i in input().split()]
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
t=[]
for i in d:
    t.append(d[i])
t.sort()
print(sum(t[0:-k]))
