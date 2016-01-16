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
a,b=map(int,raw_input().split())
if a==b:
    print 0
    exit()
#l=map(int,raw_input().split())
tmp=set([a])
n=[a]
t=[]
cnt=0
while 1:
    for i in n:
        if i-1 not in tmp:
            tmp.add(i-1)
            t.append(i-1)
        if i+1 not in tmp:
            tmp.add(i+1)
            t.append(i+1)
        if i-5 not in tmp:
            tmp.add(i-5)
            t.append(i-5)
        if i+5 not in tmp:
            tmp.add(i+5)
            t.append(i+5)
        if i-10 not in tmp:
            tmp.add(i-10)
            t.append(i-10)
        if i+10 not in tmp:
            tmp.add(i+10)
            t.append(i+10)
    n=t
    t=[]
    cnt+=1
    if b in tmp:
        print cnt
        exit()

ans=chk=0
#end = time.clock()
#print end - start
