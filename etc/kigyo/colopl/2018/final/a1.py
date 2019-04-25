#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#WA 
#100
#A


n=int(input())
s=input()
ans=chk=p=0
x=len(s)
s+=s
for i in range(x*2):
    if s[i]=="A": p+=1
    else: p=0
    print(p)
    if i<x: ans+=p
    else: chk+=p
print(ans+(chk*(n-1)))
