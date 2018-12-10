#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
ans=1
chk=0
a=[int(i) for i in input().split()]
x=y=z=0
s=[0]*1000001
#s=[0]*11
#1 2 1 3 1 4 4
while x<n:
    while z==0 and y<n:
        chk+=1
        if s[a[y]]==0:
            s[a[y]]=1
            ans=max(ans,chk)
            y+=1
        else:
            z=a[y]
            y+=1
            break
    if z==a[x]:
        z=0
    else:
        s[a[x]]=0
    chk-=1
    x+=1
    if y==n-1:
        break
print(ans)
