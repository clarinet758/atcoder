#!/usr/bin/env python
# -*- coding: UTF-8 -*-
pi=3.141592653589
n=int(raw_input())
l=[]
for i in range(n):
    l.append(int(raw_input()))
l.sort()
ans=chk=0
for a,i in enumerate(l[::-1]):
    if a%2==0:
        chk+=i**2
    else:
        chk-=i**2
print chk*pi
