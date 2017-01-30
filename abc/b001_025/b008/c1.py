#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import itertools

n=input()
l=[]
for i in range(n):
    l.append(input())

tmp=list(itertools.permutations(l))
ans=0
for i in tmp:
    c=0
    w=[1]*n
    while c<n:
        for j in range(c+1,n):
            if i[j]%i[c]==0:
                w[j]=w[j]^1
        c+=1
    ans+=w.count(1)
print ans*1.0/len(tmp)
