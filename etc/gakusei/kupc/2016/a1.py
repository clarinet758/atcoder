#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


n,a,b=map(int,input().split())
ans=0
for i in range(n):
    t=int(input())
    if t<a or t>=b: ans+=1
print(ans)
