#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n,c,k=map(int,input().split())
x=[0]*2
ans=0
l=[]
for i in range(n):
    n=int(input())
    l.append(n)
l.sort()


for n in l:
    if x[0]==0 and c>1:
        x=[n,1]
    elif x[0]==0:
        ans+=1
    elif n>x[0]+k:
        ans+=1
        x=[n,1]
    elif x[1]+1<c:
        x[1]+=1
    else:
        ans+=1
        x=[0,0]
print(ans+[0,1][x[0]>0])
