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
d=div(n)
ans=0
for i in d:
    x=i-1
    if x!=0 and n//x==n%x: ans+=x
    
print(ans)
