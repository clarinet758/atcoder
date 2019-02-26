#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
l=[int(i) for i in input().split()]
x=ans=min(l)
while 1:
    t=[-1,-1]
    for i,j in enumerate(l):
        if j%x and ans>j%x:
            ans=j%x
            t[0]=i
            t[1]=ans
    l[t[0]]=ans
    x=ans
    if t[0]==-1: break


print(x)
