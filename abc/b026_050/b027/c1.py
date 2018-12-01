#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
s=bin(n)[2:]
ans=["Takahashi","Aoki"]
if len(s)%2:
    f=1
    for a,i in enumerate(s):
        if a%2 and i=="0":
            f=0
            break
        elif a!=0 and a%2==0 and i=="1":
            break
    print(ans[f])
else:
    f=0
    for a,i in enumerate(s):
        if a%2 and i=="1":
            break
        elif a%2==0 and i=="0":
            f=1
            break
    print(ans[f])
