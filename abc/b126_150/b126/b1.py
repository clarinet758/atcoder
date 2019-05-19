#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

s=int(input())
a=s//100
b=s%100
if 0<a<13 and 0<b<13:
    print("AMBIGUOUS")
elif a==b==0 or (a>12 and b>12) or (a==0 and b>12) or (a>12 and b==0):
    print("NA")
elif a>12 and b<13 or (a==0 and 0<b<13):
    print("YYMM")
elif b>12 and a<13 or (b==0 and 0<a<13):
    print("MMYY")
