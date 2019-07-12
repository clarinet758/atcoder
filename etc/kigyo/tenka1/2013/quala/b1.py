#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
ans=0
for i in range(n):
    v=[int(i) for i in input().split()]
    if sum(v)<20: ans+=1
print(ans)
