#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
ans=chk=0
d=set()
l=[int(i) for i in input().split()]
for i in range(n):
    a,b=min(i+1,l[i]),max(i+1,l[i])
    if (a,b) in d:
        ans+=1
    else:
        d.add((a,b))
print(ans)
