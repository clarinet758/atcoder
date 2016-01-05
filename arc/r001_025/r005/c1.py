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
#l=map(int,raw_input().split())
h,w=map(int,raw_input().split())
Q=[[],[],[]]
ido=[[9]*w for _ in range(h)]
l=[]
for i in range(h):
    t=raw_input()
    if 's' in t:
        Q[0].append((i,t.index('s')))
        ido[i][t.index('s')]=0
    l.append(t)


for q in Q:
    while len(q):
        y,x=q.pop()
        for a,b in xy:
            if 0<=y+a<h and 0<=x+b<w:
                if l[y+a][x+b]=='g':
                    print 'YES'
                    exit()
                elif l[y+a][x+b]=='.' and ido[y+a][x+b]==9:
                    ido[y+a][x+b]=ido[y][x]
                    Q[ido[y][x]].append((y+a,x+b))
                elif l[y+a][x+b]=='#' and ido[y][x]<2 and ido[y+a][x+b]==9:
                    ido[y+a][x+b]=ido[y][x]+1
                    Q[ido[y][x]+1].append((y+a,x+b))
print 'NO'
ans=chk=0
#end = time.clock()
#print end - start
