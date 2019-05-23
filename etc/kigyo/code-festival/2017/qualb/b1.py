#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
d=[int(i) for i in input().split()]
m=int(input())
t=[int(i) for i in input().split()]
p=1
w={}
for i in d:
    if i in w: w[i]+=1
    else: w[i]=1
for i in t:
    if i in w and w[i]>0:
        w[i]-=1
    else:
        p=0
        break
print(["NO","YES"][p])
