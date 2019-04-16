#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

input()
s=input()
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=2
ans=1
for i in d:
    ans*=d[i]
print((ans-1)%1000000007)
