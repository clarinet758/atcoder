#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
input=sys.stdin.readline
mod=1000000007
#from https://atcoder.jp/contests/chokudai_S001/submissions/1459323

n=int(input())
a=[int(i) for i in input().split()]
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

fact=[1]*(n+1)
for i in range(1,n):
    fact[i]=(fact[i-1]*i)%mod
ans=1

for i,a in enumerate(a):
    v=a-get(a)
    add(a,1)
    ans=(ans+fact[n-i-1]*(v-1))%mod
print(ans)
