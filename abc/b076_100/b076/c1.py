#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
s=list(input())
t=list(input())

a=len(s)
b=len(t)
f=0
for i in range(-1,-a+b-2,-1):
    f=0
    for j in range(-1,-b-1,-1):
        if (s[i+j+1]!="?"and t[j]!=s[i+j+1]):
            f=1
            break
    if f==1: continue
    for k in range(-1,-b-1,-1):
        s[i+k+1]=t[k]
    for p in range(a):
        if s[p]=="?":
            s[p]="a"
    print("".join(s))
    exit()
print("UNRESTORABLE")
        
