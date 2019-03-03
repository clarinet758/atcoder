#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

input()
ans=0
l=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
for i,j in zip(l,a): ans=max(ans,i*j)
print(ans)
