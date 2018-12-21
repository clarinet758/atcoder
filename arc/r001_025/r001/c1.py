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

l=[]
q=0
for i in range(8):
    tmp=list(raw_input())
    q+=tmp.count('Q')
    l.append(tmp)

def chk(y,x):
    for i in range(8):
        if i!=x and l[y][i]=='Q':
            return 0
        if i!=y and l[i][x]=='Q':
            return 0
    for i in range(1,8):
        xm,xp,ym,yp=x-i,x+i,y-i,y+i
        if ym>=0 and xm>=0 and l[ym][xm]=='Q':
            return 0
        if ym>=0 and xp<8 and l[ym][xp]=='Q':
            return 0
        if yp<8 and xm>=0 and l[yp][xm]=='Q':
            return 0
        if yp<8 and xp<8 and l[yp][xp]=='Q':
            return 0
    return 1

def dfs(nokori,cy):
    if nokori==0:
        for i in l:
            print ''.join(i)
        exit()

    for y in range(cy,8):
        for x in range(8):
            if l[y][x]=='Q' or chk(y,x)==0:
                continue
            l[y][x]='Q'
            dfs(nokori-1,y+1)
            l[y][x]='.'

for i in range(64):
    if l[i/8][i%8]=='Q' and chk(i/8,i%8)==0:
        print 'No Answer'
        exit()
q=8-q
dfs(q,0)
print 'No Answer'

exit()
n=int(raw_input())
n,k=map(int,raw_input().split())
#l=map(int,raw_input().split())
ans=chk=0
#end = time.clock()
#print end - start
