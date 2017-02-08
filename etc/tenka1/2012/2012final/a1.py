#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

#TLE!!!!

mod=1000000007
n=int(input())
 
def getfib(k):
    if k==0: return 1
    if k==1: return 2
    if (fib[k]!=0): return fib[k]
    return getfib(k-1)+getfib(k-2)
 
def sol(k):
    if k==0: return 0
    ret=mod
    for i in range(25):
        if k<getfib(i): break
        ret=min(ret, sol(k-getfib(i))+1)
    return ret
 
fib=[0]*25
for i in range(1,25):
    fib[i]=getfib(i)
print(sol(n))


