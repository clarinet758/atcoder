#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
ans=set([])
i=1
while i**2<=n:
    if n%i==0:
        ans.add(i)
        ans.add(n//i)
    i+=1

ans=list(ans)
ans.sort()
for i in ans:
    print(i)

