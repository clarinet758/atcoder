#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


x,k,d=map(int,input().split())
x=abs(x)
ans=0
if x>k*d:
    print(x-k*d)
else:
    a=x//d
    p=x-d*a
    q=abs(x-d*a-d)
    print(q if (k-a)%2 else p)
