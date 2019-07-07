#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


mod=2019
l,r=map(int,input().split())
d={}
for i in range(l,min(r+1,l+2020)):
    w=i%2019
    if w in d:
        d[w]+=1
    else:
        d[w]=1
ans=2020
for i in d:
    for j in d:
        if i!=j:
            ans=min(ans,i*j%mod)
        elif i==j and d[i]>1:
            ans=min(ans,i*j%mod)
print(ans)
