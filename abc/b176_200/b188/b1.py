#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
ans=0
for i in range(n):
    ans+=a[i]*b[i]
print("Yes" if ans==0 else "No")
