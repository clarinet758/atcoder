#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#from abc093/submissions/2330255
q=int(input())
for i in range(q):
    a,b=map(int,input().split())
    c=int((a*b)**0.5)
    if c*(c+1)<a*b: print(2*c-1)
    elif a*b==c*c and a!=b: print(2*c-3)
    else: print(2*c-2)
