#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
a=[int(i) for i in input().split()]
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
ans=chk=0
for i in d:
    ans+=[d[i],d[i]-i][d[i]>=i] 
print(ans)
