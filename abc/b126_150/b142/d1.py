#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import fractions
# fractions.gcd(x,y)

def div(n):
    divisors = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.add(i)
            if i != n // i:
                divisors.add(n//i)

    return divisors
a,b=map(int,input().split())
x=div(a)
y=div(b)
z=list(x&y)
z.sort()
t=len(z)
ans=1
for i in range(1,t):
    f=1
    for j in range(1,i):
        if (z[i]%z[j]==0):
            f=0
            break
    if f:
        ans+=1
print(ans)
