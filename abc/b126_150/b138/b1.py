#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import fractions
def gcd(x,y): return fractions.gcd(x,y)
def lcm(a,b): return a*b//fractions.gcd(a,b)

n=int(input())
a=[int(i) for i in input().split()]
x=a[0]
for i in range(1,n):
    x=lcm(x,a[i])
ans=chk=0
for i in a:
    ans+=x//i
print(x/ans)
