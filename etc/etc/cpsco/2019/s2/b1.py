#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
ans=[0,1]
for i in range(n):
    c,a=map(str,input().split())
    if c=="*" and a!="0": ans[1]*=int(a)
    elif c=="+": ans[0]+=int(a)
print(ans[0]*ans[1])
