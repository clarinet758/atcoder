#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
#sys.stdin=file('input.txt')
#sys.stdout=file('output.txt','w')
#10**9+7
mod=1000000007
#mod=1777777777
pi=3.141592653589
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
#start = time.clock()

def sol(sx,sy,gx,gy):
    return (abs(gx-sx)**2+abs(gy-sy)**2)**0.5
l=map(int,raw_input().split())
n=int(raw_input())
for i in range(n):
    x,y=map(int,raw_input().split())
    chk=(sol(l[0],l[1],x,y)+sol(x,y,l[2],l[3]))/l[4]
    if l[5]>chk:
        print 'YES'
        exit()
print 'NO'

ans=0
#end = time.clock()
#print end - start
