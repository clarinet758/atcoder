#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
input=sys.stdin.readline

n=int(input())
a=[int(i) for i in input().split()]
ans=0
t=a[0]
for i in range(1,n):
    ans+=a[i]-t
    t=a[i]
print(ans/(n-1))
