#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b//gcd(a,b)
n,m=map(int,input().split())
s=input()
t=input()
l=lcm(n,m)
d={}
f=l
for i in range(max(n,m)):
    o=i*(l//n)
    p=i*(l//m)
    if i<n and o not in d:
        d[o]=s[i]
    elif i<n and o in d and d[o]!=s[i]:
        f=-1
    if i<m and p not in d:
        d[p]=t[i]
    elif i<n and p in d and d[p]!=t[i]:
        f=-1
print(f)
