#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
input=sys.stdin.readline
def prime_t(t):
    i=2
    while i**2<=t:
        if t%i==0:
            return 0
        i+=1
    return 1

def prime_list(tt):
    p_list=[]
    for i in range(2,tt+1):
        if prime_t(i):
            p_list.append(i)
    return p_list

n=int(input())
ans=prime_list(n-1)
print(len(ans))
