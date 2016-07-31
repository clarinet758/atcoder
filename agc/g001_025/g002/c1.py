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

#n=int(raw_input())
n,l=map(int,raw_input().split())
a=map(int,raw_input().split())
w=sum(a)
x=1
y=n-1
f=0
ans=[]
while 1:
    if a[x-1]<a[y]:
        if w>=l:
            ans.append(x)
            w-=a[x-1]
            x+=1
        else:
            break
    else:
        if w>=l:
            ans.append(y)
            w-=a[y]
            y-=1
        else:
            break
    if x==y+1:
        f=1
        break
if f==0:
    print 'Impossible'
else:
    print 'Possible'
    for i in ans:
        print i



ans=chk=0
#end = time.clock()
#print end - start
