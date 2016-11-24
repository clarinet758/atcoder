#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n=int(raw_input())
ans=10**9
tmp=int(n**0.5)
for i in range(1,tmp+20):
    for j in range(tmp+20,0,-1):
        if 0<i*j<=n:
            ans=min(ans,n-i*j+abs(i-j))
print ans
