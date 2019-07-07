#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,d=map(int,input().split())
w=[]
for i in range(n):
    l=[int(i) for i in input().split()]
    w.append(l)
ans=chk=0
for i in range(n-1):
    for j in range(i+1,n):
        x=0
        for k in range(d):
            x+=(w[i][k]-w[j][k])**2
        ans+=[0,1][x==int(pow(x,0.5))**2]
print(ans)
