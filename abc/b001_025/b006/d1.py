#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import bisect

def lis(c):
    l=[]
    l.append(c[0])
    ans=1
    for i in range(1,n):
        if l[ans-1]<c[i]:
            l.append(c[i])
            ans+=1
        else:
            tmp=bisect.bisect_right(l,c[i])
            l[tmp]=c[i]
    return ans

n=int(raw_input())
N=range(1,n)
c=[]
for i in range(n):
    c.append(int(raw_input()))
print n-lis(c)

