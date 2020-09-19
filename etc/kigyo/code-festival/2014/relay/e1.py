#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

h,w=map(int,input().split())
ans=0
for i in range(h):
    for j in input():
        if j!=".": ans+=int(j)
print(ans)
