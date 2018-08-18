#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
p=5000000000000000
s=input()
k=int(input())

chk=1
ans=f=0
for i in s:
    chk=1
    if i=="1": 
        ans+=1
        continue
    for j in range(p):
        chk*=int(i)
        if ans+chk>=k:
            print(i)
            f=1
            break
    ans+=chk
    if f==1: break
if f==0: print(s[-1])
