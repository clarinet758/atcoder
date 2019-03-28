#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
s=input()
d=[0,0]
for i in s:
    if i=="(": d[0]+=1
    if i==")" and d[0]>0: d[0]-=1
for i in s[::-1]:
    if i==")": d[1]+=1
    if i=="(" and d[1]>0: d[1]-=1
s="("*d[1]+s+")"*d[0]
print(s)
