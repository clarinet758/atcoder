#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-
def prime_t(t):
    i=2
    while i**2<=t:
        if t%i==0:
            return 0
        i+=1
    return 1
p=[]

for i in range(2,1008):
    if prime_t(i):
        p.append(i)
d={i:0 for i in p}
mod=10**9+7
n=int(input())
tmp=1
ans=1
R=[i for i in range(168)]
for i in range(1,n+1):
    tmp*=i
    for j in R:
        while tmp%p[j]==0:
            d[p[j]]+=1
            tmp//=p[j]
        if tmp<p[j]:
            break
for i in d:
    ans*=(d[i]+1)
    ans%=mod
print(ans)
