#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def sig(a): return a*(a+1)//2
n=int(input())
ans=0
for i in range(n):
    a,b=map(int,input().split())
    ans+=sig(b)-sig(a-1)
print(ans)
