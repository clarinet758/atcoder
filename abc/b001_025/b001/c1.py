#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

news=["NNW","NW","WNW","W","WSW","SW","SSW","S","SSE","SE","ESE","E","ENE","NE","NNE","N"][::-1]
g,s=map(int,input().split())
r=news[((g*10+1125)%36000)//2250]
s=s*10//6

if s<=24:
    w=0
elif s<=154:
    w=1
elif s<=334:
    w=2
elif s<=544:
    w=3
elif s<=794:
    w=4
elif  s<=1074:
    w=5
elif s<=1384:
    w=6
elif s<=1714:
    w=7
elif s<=2074:
    w=8
elif s<=2444:
    w=9
elif s<=2844:
    w=10
elif s<=3264:
    w=11
else:
    w=12

if w==0: r="C"
print(r,w)
