#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
for i in range(1,n+1):
    t=""
    if i%2==0: t+="a"
    if i%3==0: t+="b"
    if i%4==0: t+="c"
    if i%5==0: t+="d"
    if i%6==0: t+="e"
    if len(t): print(t)
    else: print(i)
    
