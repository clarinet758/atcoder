#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
a=[int(i) for i in input().split()]
ans=10**9
for i in a:
    tmp=0
    while i%2==0:
        tmp+=1
        i//=2
    ans=min(ans,tmp)
print(ans)
"""

def sol(i):
    tmp=0
    while i%2==0:
        tmp+=1
        i//=2
    return tmp

input()
print(min([sol(int(i)) for i in input().split()]))
"""
