#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n=input()
ans,cnt='',0
d={}
for i in range(n):
    s=raw_input()
    if s in d:
        d[s]+=1
    else:
        d[s]=1
    if  d[s]>cnt:
        cnt=d[s]
        ans=s
print ans
