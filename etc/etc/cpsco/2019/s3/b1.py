#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,m=map(int,input().split())
l=[int(i) for i in input().split()]
l.sort(reverse=True)
ans=0
for i in l:
    ans+=1
    m-=i
    if m<=0: break
print(ans)
