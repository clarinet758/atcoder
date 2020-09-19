#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
input=sys.stdin.readline

cnt=[0]*30
n=int(input())
a=[int(i) for i in input().split()]
for i in a:
    x=(bin(i)[2:])[::-1]
    for j,k in enumerate(x):
        if k=="1":
            cnt[j]=(cnt[j]+1)%2

print("No" if any(cnt) else "Yes")
