#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def div(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
 
    return divisors
 
n=int(input())
at=[int(i) for i in input().split()]
a=set(at)
d={}
for i,j in enumerate(a):
    t=div(j)
    for k in t:
        if k in d:
            d[k]+=1
        elif i==0 or k not in d:
            d[k]=1
ans=1
for i in d:
    x=0
    for j in at:
        if j%i: x+=1
    if x<2: ans=max(ans,i)
print(ans)
