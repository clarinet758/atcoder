#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
s=[]
for i in range(366):
    if i%7==0 or i%7==6: s.append(1)
    else: s.append(0)
l=[0,31,29,31,30,31,30,31,31,30,31,30,31]
for i in range(n):
    m,d=input().split("/")
    m=int(m)
    d=int(d)
    x=sum(l[:m])
    for j in range(x+d-1,366):
        if s[j]==0:
            s[j]=1
            break
ans=2
tmp=0
for i in s:
    if i==1: tmp+=1
    else: tmp=0
    ans=max(ans,tmp)
print(ans)
