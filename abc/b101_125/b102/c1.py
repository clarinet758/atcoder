#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
a=[int(i)-p for p,i in enumerate(input().split())]
a.sort()
ans=0
for i in a:
    ans+=abs(i-a[n//2])
print(ans)
