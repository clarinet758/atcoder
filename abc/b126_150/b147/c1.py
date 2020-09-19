#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
w=[]
ans=chk=0
for i in range(n):
    a=int(input())
    t=[]
    for j in range(a):
        x,y=map(int,input().split())
        t.append((x,y))
    w.append(t)
for i in range(1,2**n):
    l=[0]*n
    for j in range(n):
        if i&1: l[j]=1
        i=i>>1
    chk=1
    for j in range(n):
        if l[j]:
            for k in w[j]:
                if l[k[0]-1]!=k[1]:
                    chk=0
                    break
    if chk: ans=max(ans,sum(l))
print(ans)
