#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
s=input()
k=int(input())
x=-1
y=""
for a,i in enumerate(s):
    if i!="1":
        x=a
        y=i
        break
        
if x!=-1 and x+1<=k: print(y)
else: print(1)
