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
def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)
def euclid_dis(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0

h,w=map(int,raw_input().split())
l=[]
H=range(h)
for i in H:
    l.append(raw_input())

ans=[['.']*w for i in H]
tenkai=[['.']*w for i in H]
news=[(0,0)]+xy+bs

def sol(y,x):
    for a,b in news:
        if 0<=y+a<h and 0<=x+b<w:
            if l[y+a][x+b]=='.':
                return 0
    return 1

for i in H:
    for j in range(w):
        if sol(i,j):
            ans[i][j]='#'

for i in H:
    for j in range(w):
        if ans[i][j]=='#':
            for a,b in news:
                if 0<=i+a<h and 0<=j+b<w:
                    tenkai[i+a][j+b]='#'
for i in H:
    if ''.join(tenkai[i])!=l[i]:
        print 'impossible'
        exit()
print 'possible'
for i in ans:
    print ''.join(i)






ans=chk=0
#end = time.clock()
#print end - start
