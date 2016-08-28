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
def bin01(a,b): return '0'*(b-len(bin(a))+2)+bin(a)[2:]
def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)
def euclid_dis(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0

#n=int(raw_input())
n,a=map(int,raw_input().split())

print bin01(n,a)
exit()
x=map(int,raw_input().split())
x.sort()
ans=0

for i in range(1<<n):
    chk=0
    t=bin(i)[2:]
    t='0'*(n-len(t))+t
    for j,p in enumerate(t):
        if p=='1':
            chk+=x[j]
    if chk!=0 and chk==a*t.count('1'):
        ans+=1
print ans

    

#end = time.clock()
#print end - start
