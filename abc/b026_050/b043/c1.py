#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
a=[int(i) for i in input().split()]
d=sum(a)
t=[d//n,d//n+1]
ans=[0]*2
for i in a:
    ans[0]+=(i-t[0])**2
    ans[1]+=(i-t[1])**2
print(min(ans))
