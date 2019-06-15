#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


n=int(input())
w={}
d=[]
for i in range(n):
    x,y=map(int, input().split())
    d.append((x,y))

chk=0
for i in range(n):
    a=d[i][0]
    b=d[i][1]
    for j in range(n):
        if i==j: continue
        p=d[j][0]
        q=d[j][1]
        if (a-p,b-q) in w:
            w[(a-p,b-q)]+=1
        else:
            w[(a-p,b-q)]=1
        chk=max(chk,w[(a-p,b-q)])
print(n-chk)
