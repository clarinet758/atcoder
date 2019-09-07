#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
c=[int(i) for i in input().split()]
ans=chk=0
for i in range(n):
    ans+=b[a[i]-1]
    if i!=0 and a[i-1]+1==a[i]:
        ans+=c[a[i-1]-1]
print(ans)
