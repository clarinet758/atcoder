#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,k=map(int,input().split())
a=[int(i) for i in input().split()]
ans=chk=0
a.sort(reverse=True)
for i in range(n):
    ans+=a[i]
    if ans>=k:
        print(i+1)
        exit()
print(-1)
