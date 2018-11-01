#!/usr/bin/env python3


def prime(t):
    i=2
    while i**2<=t:
        if t%i==0: return 0
        i+=1
    return 1

mod=10**9+7

p=[]
for i in range(2,1008):
    if prime(i):
        p.append(i)

d={i:0 for i in p}
n=int(input())

ans=tmp=1
for i in range(1,n+1):
    tmp*=i
    for j in p:
        while tmp%j==0:
            d[j]+=1
            tmp//=j
        if tmp<j: break

for i in d:
    ans*=d[i]+1
    ans%=mod
print(ans) 
