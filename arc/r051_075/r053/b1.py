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

s=raw_input()
l={}
for i in s:
    if l.has_key(i):
        l[i]+=1
    else:
        l[i]=1
ans=chk=cnt=0
for i in l:
    if l[i]%2==1:
        chk+=1
        l[i]-=1
    cnt+=l[i]/2
if chk==0:
    print len(s)
    exit()
print (cnt/chk)*2+1
#n,k=map(int,raw_input().split())
#l=map(int,raw_input().split())
#end = time.clock()
#print end - start
