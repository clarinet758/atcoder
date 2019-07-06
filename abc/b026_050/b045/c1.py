#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

s=input()
ans=chk=0
for i in range(2**(len(s)-1)):
    d=bin(i)[2:]
    d=("0"*(9-len(d))+d)[::-1]
    t=int(s[0])
    for i in range(len(s)-1):
        if d[i]=="0":
            t*=10
            t+=int(s[i+1])
        else:
            ans+=t
            t=int(s[i+1])
    ans+=t

print(ans)
