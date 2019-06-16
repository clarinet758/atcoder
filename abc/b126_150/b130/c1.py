#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

w,h,x,y=map(int,input().split())
s=(w*h)/2
if (h//2==y and h%2==0) and (w//2==x and w%x==0):
    print(s,1)
else:
    print(s,0)
