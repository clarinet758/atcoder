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
def niten(a,b): return abs(a-b) if a>=0 and b>=0 else  a+abs(b) if a>=0 else abs(a)+b if b>=0 else abs(abs(a)-abs(b))
def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)
def euclid_dis(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0

a=raw_input()
b=raw_input()
c=raw_input()
f=0
while 1:
#    print a,b,c
    if f==0:
        if len(a)==0:
            print 'A'
            break
        elif a[0]=='b':
            f=1
        elif a[0]=='c':
            f=2
        a=a[1:]
    elif f==1:
        if len(b)==0:
            print 'B'
            break
        elif b[0]=='a':
            f=0
        elif b[0]=='c':
            f=2
        b=b[1:]
    else:
        if len(c)==0:
            print 'C'
            break
        elif c[0]=='a':
            f=0
        elif c[0]=='b':
            f=1
        c=c[1:]


n,k=map(int,raw_input().split())
l=map(int,raw_input().split())
ans=chk=0
#end = time.clock()
#print end - start
