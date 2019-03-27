#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def prime_t(t):
    i=2
    while i**2<=t:
        if t%i==0:
            return 0
        i+=1
    return 1
d=set([])
n=10**5+1
p=[0]*(10**5+1)
for i in range(2,n):
    if prime_t(i):
        d.add(i)
    if (i in d and (i+1)//2 in d): p[i]=p[i-1]+1
    else: p[i]=p[i-1]

q=int(input())
for i in range(q):
    ans=0
    l,r=map(int,input().split())
    print(p[r]-p[l-1])
