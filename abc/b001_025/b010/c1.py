#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
#10**9+7
mod=1000000007
#start = time.clock()
txa,tya,txb,tyb,T,V=map(int,raw_input().split())
n=int(raw_input())
for i in range(n):
    x,y=map(int, raw_input().split())
    to=((x-txa)**2+(y-tya)**2)**0.5+((txb-x)**2+(tyb-y)**2)**0.5
    if to<=T*V:
        print 'YES'
        exit()
print 'NO'

ans=chk=0
#end = time.clock()
#print end - start
