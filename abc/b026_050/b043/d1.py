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

s=raw_input()
tmp=[s[0], s[1]]
chk=len(s)
if tmp[0]==tmp[1]:
    print 1,2
elif chk==3 and len(set(list(s)))<3:
    print 1,3
elif chk<4:
    print -1,-1
else:
    for i in range(2,chk):
        if len(tmp)==3:
            tmp.pop(0)
        tmp.append(s[i])
        if len(set(tmp))<3:
            print i-1,i+1
            exit()
    else:
        print -1,-1
#l=map(int,raw_input().split())
ans=chk=0
#end = time.clock()
#print end - start
