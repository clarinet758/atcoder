#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
input=sys.stdin.readline

## from https://atcoder.jp/contests/chokudai_S001/submissions/1459166

n=int(input())
*a,=map(int,input().split())
data=[0]*(n+1)
def add(i,x):
    while i<=n:
        data[i]+=x
        i+=i&-i

def get(i):
    s=0
    while i:
        s+=data[i]
        i-=i&-i
    return s

ans=0
for x in a:
    add(x,1)
    ans+=x-get(x)
print(ans)
