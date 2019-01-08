#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,w=map(int,input().split())
d=[]
dp=[0]*(w+1)
ans=chk=0
for i in range(n):
    a,b=map(int,input().split())
    d.append((a,b))
d.sort()
print(ans)
