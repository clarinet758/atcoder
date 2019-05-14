#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

s=input()
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
t=d[i]
for i in d:
    if t!=d[i]:
        print("No")
        exit()
print("Yes")
