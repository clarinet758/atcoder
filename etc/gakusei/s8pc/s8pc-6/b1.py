#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
l,r=set([]),set([])
d=[]
for i in range(n):
    a,b=map(int,input().split())
    d.append((a,b))
    l.add(a)
    r.add(b)
ans=chk=-1
for i in l:
    for j in r:
        chk=0
        for k in range(n):
            chk+=abs(i-d[k][0])+(d[k][1]-d[k][0])+abs(j-d[k][1])
        if ans==-1: ans=chk
        else: ans=min(ans,chk)
print(ans)
