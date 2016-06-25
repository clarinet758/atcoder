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
r,c=map(int,raw_input().split())
sy,sx=map(int,raw_input().split())
gy,gx=map(int,raw_input().split())
q=set([(sy-1,sx-1)])
#l=map(int,raw_input().split())
l=[]
for i in range(r):
    l.append(list(raw_input()))
l[sy-1][sx-1]=0
while len(q):
    ny,nx=q.pop()
    for y,x in xy:
        iy,ix=ny+y,nx+x
        if 0<iy<r-1 and 0<ix<c-1:
            if l[iy][ix]=='.':
                l[iy][ix]=l[ny][nx]+1
                q.add((iy,ix))
            elif type(l[iy][ix])==int:
                #l[iy][ix]=min(l[iy][ix],l[ny][nx]+1)
                if l[iy][ix]>l[ny][nx]+1:
                    l[iy][ix]=l[ny][nx]+1
                    q.add((iy,ix))
print l[gy-1][gx-1]

ans=chk=0
#end = time.clock()
#print end - start
