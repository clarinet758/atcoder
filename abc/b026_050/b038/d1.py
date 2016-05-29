#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
import collections
import bisect
#sys.stdin=file('input.txt')
#sys.stdout=file('output.txt','w')
#10**9+7
mod=1000000007
#mod=1777777777
pi=3.141592653589
IS=float('inf')
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)
def euclid_dis(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0
##746747 roto_37さんをパクリ

n=int(raw_input())
l=range(n)
wh1=[]
for i in l:
    w,h=map(int,raw_input().split())
    wh1.append([-w,h])
wh1.sort()
wh=wh1[::-1]
dp=[IS]*n
for i in l:
    dp[bisect.bisect_left(dp,wh[i][1])]=wh[i][1]
print len(set(dp))-1 if IS in dp else len(dp)
exit()
for i in l:
    if dp[i]==IS:
        i-=1
        break
print i+1

exit()
#end = time.clock()
#print end - start
