#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n,a,b=map(int,input().split())
if (n==1 and a!=b) or (a>b):
    print(0)
else:
    print((b+b*(n-2)+a)-(b+a+a*(n-2))+1)
