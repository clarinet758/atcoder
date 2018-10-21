#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
k,s=map(int,input().split())
ans=chk=0
for i in range(k+1):
    for j in range(k+1):
        if (0<=s-i-j<=k): ans+=1
print(ans)
