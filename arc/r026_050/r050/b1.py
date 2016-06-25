#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
import collections
#sys.stdin=file('input.txt')
#sys.stdout=file('output.txt','w')
#10**9+7
mod=1000000007
#mod=1777777777
pi=3.141592653589
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)
def euclid_dis(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0

#n=int(raw_input())
R,B=map(int,raw_input().split())
x,y=map(int,raw_input().split())
#l=map(int,raw_input().split())
ans=0
t1=min(R/x,B)
R-=t1*x
B-=t1
t2=min(R,B/y)
ans=t1+t2
R-=t2
B-=t2*y
while 1:
    if t1>0:
        t1-=1
        R+=x
        B+=1
        if R>0 and B>=y:
            tmp=min(R,B/y)
            R-=tmp
            B-=y*tmp
            t2+=tmp
        ans=max(ans,t1+t2)
    else:
        break
print ans



#end = time.clock()
#print end - start
