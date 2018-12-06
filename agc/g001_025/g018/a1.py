#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,k=map(int,input().split())
a=[int(i) for i in input().split()]
if k>max(a):
    print("IMPOSSIBLE")
    exit()
if k in a:
    print("POSSIBLE")
    exit()
for i in range(n-1):
    for j in range(i+1,n):
        t=abs(a[i]-a[j])
        if (t): k%=abs(a[i]-a[j])
print(["IMPOSSIBLE","POSSIBLE"][k==0])
