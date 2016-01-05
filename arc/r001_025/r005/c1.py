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
h,w=map(int,raw_input().split())
#l=map(int,raw_input().split())
l,Q=[],[[],[],[]]
D=[[9]*w for _ in range(h)]

for i in range(h):
    t=list(raw_input())
    if 's' in t:
        Q[0].append((i,t.index('s')))
        D[i][t.index('s')]=0
        t[t.index('s')]=0
    if 'g' in t:
        gy=i
        gx=t.index('g')
    l.append(t)

for q in Q:
    while len(q):
        y,x=q.pop()
        for iy,ix in xy:
            iy+=y
            ix+=x
            if 0<=iy<h and 0<=ix<w:
                if l[iy][ix]=='#':
                    d=D[y][x]+1
                else:
                    d=D[y][x]
                if d<=2 and d<D[iy][ix]:
                    D[iy][ix]=d
                    Q[d].append((iy,ix))


print 'YES' if D[gy][gx]<=2 else 'NO'
ans=chk=0
#end = time.clock()
#print end - start
