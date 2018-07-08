#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b//gcd(a,b)
n=int(input())
ans=1
for i in range(n):
    t=int(input())
    ans=lcm(ans,t)
print(ans)
