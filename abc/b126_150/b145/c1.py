#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import itertools

n=int(input())
l=[int(i) for i in range(n)]
ans=chk=p=0
w=[]
for i in range(n):
    x,y=map(int,input().split())
    w.append((x,y))
for i in list(itertools.permutations(l,n)):
    chk=0
    for j in range(n-1):
        chk+=((w[i[j]][0]-w[i[j+1]][0])**2+(w[i[j]][1]-w[i[j+1]][1])**2)**0.5
    ans+=chk
    p+=1
    
print(ans/p)
