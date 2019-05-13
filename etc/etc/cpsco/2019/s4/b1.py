#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,d=map(int,input().split())
w=[]
for i in range(d):
    s=input()
    p=0
    for j in range(n):
        if s[j]=="o": 
            p+=2**j
    w.append(p)
ans=0
for i in range(d-1):
    for j in range(i+1,d):
        ans=max(ans,bin(w[i]|w[j]).count("1"))
print(ans)
