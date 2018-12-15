#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
s=input()
x=len(s)
b=[0]*x
for i in range(-1,-x-1,-1):
    if i==-1and s[i]=="W": b[-1]=1
    elif s[i]=="W": b[i]=b[i+1]+1
    else: b[i]=b[i+1]
ans=chk=0
for i in range(x):
    if s[i]=="B":
        ans+=b[i]
print(ans)
