#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,m=map(int,input().split())
l=[int(i) for i in input().split()]
l.sort()
ans=[0]
for i in range(m-1):
    ans.append(l[i+1]-l[i])
ans.sort()
for i in range(n-1):
    if len(ans)==1: break
    ans.pop()
print(sum(ans))
