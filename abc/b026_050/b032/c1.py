#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,k=map(int,input().split())
s=[]
for i in range(n):
    j=int(input())
    if j==0:
        print(n)
        exit()
    s.append(j)
ans=chk=0
t=-1
p=1
for i in range(n):
    p*=s[i]
    chk+=1
    #print(p)
    if p<=k:
        ans=max(ans,chk)
    else:
        while p>k and t<i:
            t+=1
            p//=s[t]
            chk-=1
        ans=max(ans,chk)
print(ans)
