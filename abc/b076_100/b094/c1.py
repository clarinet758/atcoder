#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# pscl 要修正

n=int(input())
x=[int(i) for i in input().split()]
if n==2:
    for i in x[::-1]:
        print(i)
    exit()

d={}
y=sorted(x)

ans={}
for a,i in enumerate(y):
    if a<n//2:
        if i not in ans:
            ans[i]=y[n//2]
    elif a>=n//2:
        if i not in ans:
            ans[i]=y[n//2-1]

for i in x:
    print(ans[i])

