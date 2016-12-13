#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import sys
import io
import re
import math
#start = time.clock()
m = map(float, raw_input().split())
k = float(m[1])/60.0
#k=round(k,1)
h = int(m[0])/10.0
h=round(h,2)
if h>=348.75 or h<11.25: i = 'N'
elif h<33.75: i = 'NNE'
elif h<56.25: i = 'NE'
elif h<78.75: i='ENE'
elif h<101.25: i='E'
elif h<123.75: i='ESE'
elif h<146.25: i='SE'
elif h<168.75: i='SSE'
elif h<191.25: i='S'
elif h<213.75: i='SSW'
elif h<236.25: i='SW'
elif h<258.75: i='WSW'
elif h<281.25: i='W'
elif h<303.75: i='WNW'
elif h<326.25: i='NW'
elif h<348.75: i='NNW'
 
if k<=0.24: z=0
elif k<=1.54: z=1
elif k<=3.34: z=2
elif k<=5.44: z=3
elif k<=7.94: z=4
elif k<=10.74: z=5
elif k<=13.84: z=6
elif k<=17.14: z=7
elif k<=20.74: z=8
elif k<=24.44: z=9
elif k<=28.44: z=10
elif k<=32.64: z=11
else: z=12
if z>0: print i,z
else: print 'C',z

