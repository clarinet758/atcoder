#!/usr/bin/env python
# -*- coding: UTF-8 -*-
n=int(raw_input())
l=[]
for i in range(n):
    l.append(raw_input())

for i in range(n):
    tmp=''
    for j in range(n):
        tmp+=l[j*-1-1][i]
    print tmp
