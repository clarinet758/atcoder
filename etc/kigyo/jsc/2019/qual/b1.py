#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

mod=1000000007

n,k=map(int,input().split())
a=[int(i) for i in input().split()]
b=a*2
ans=chk=0
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]>a[j]:
            chk+=1
            chk%=mod

for i in range(n):
    for j in range(n,n*2):
        if b[i]>b[j]:
            ans+=1
            ans%=mod
t=k-1
t=t*(t+1)//2
print((chk*k%mod+ans*t%mod)%mod)
