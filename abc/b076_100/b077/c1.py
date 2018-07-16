#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import bisect
n=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
c=[int(i) for i in input().split()]
a.sort()
b.sort()
b=b[::-1]
c.sort()
ans=tmp=0
for i in b:
    x=bisect.bisect_left(a,i)
    y=bisect.bisect_right(c, i)
    ans+=x*(n-y)
print(ans)
