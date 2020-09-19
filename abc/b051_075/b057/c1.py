#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
ans=1000
for i in range(1,100001):
    if n%i==0:
        ans=min(ans,len(str(max(n//i,i))))
print(ans)
