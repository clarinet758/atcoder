#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,h=map(int,input().split())
a=[]
b=[]
for i in range(n):
    x,y=map(int,input().split())
    a.append(x)
    b.append(y)
a.sort()
b.sort()
chk=max(a)
ans=0
for i in b[::-1]:
    if (h<=0 or i<chk): break
    ans+=1
    h-=i
if h>0:
    ans+=(h+chk-1)//chk
    
print(ans)
