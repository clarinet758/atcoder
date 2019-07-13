#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
a=[int(i)-1 for i in input().split()]
data=[0]*(n)
ans=0
for x in range(n):
    y=x
    data[y]=1
    while a[y]!=y:
        y=a[y]
        if data[y]: break
        data[y]=1
        ans+=1
print("YES" if (n-ans)%2==0 else "NO")
