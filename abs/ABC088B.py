#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
a=[int(i) for i in input().split()]
a.sort()
ans=0
for i,j in enumerate(a[::-1]):
    if i%2: ans-=j
    else:   ans+=j
print(ans)
