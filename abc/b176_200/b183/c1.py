#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import itertools
n,k=map(int,input().split())
p=[i for i in range(1,n)]
t=[]
for i in range(n):
    l=[int(i) for i in input().split()]
    t.append(l)
ans=chk=0
for i in list(itertools.permutations(p)):
    chk=0
    chk+=t[0][i[0]]
    chk+=t[i[-1]][0]
    for j in range(n-2):
        chk+=t[i[j]][i[j+1]]
    if chk==k:
        ans+=1
print(ans)
