#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,d=map(int,input().split())
w=[]
for i in range(n):
    l=[int(i) for i in input().split()]
    w.append(l)
ans=0
chk=set([int(i)**2 for i in range(0,401,1)])
for i in range(n-1):
    for j in range(i+1,n):
        cnt=0
        for k in range(d):
            cnt+=(w[i][k]-w[j][k])**2
        if cnt in chk:
            ans+=1 
print(ans)
