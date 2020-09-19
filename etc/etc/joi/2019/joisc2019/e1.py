#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
input=sys.stdin.readline
sys.setrecursionlimit(3000)
import re
import math
import collections
import bisect
import fractions
#sys.stdin=file('input.txt')
#sys.stdout=file('output.txt','w')
#10**9+7
mod=1000000007
#mod=1777777777
pi=3.1415926535897932
IS=float('inf')
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
def niten(a,b): return abs(a-b) if a>=0 and b>=0 else  a+abs(b) if a>=0 else abs(a)+b if b>=0 else abs(abs(a)-abs(b))
def fib(n): return [(seq.append(seq[i-2] + seq[i-1]), seq[i-2])[1] for seq in [[0, 1]] for i in range(2, n)]
# fractions.gcd(x,y)
def lcm(a,b): return a*b//fractions.gcd(a,b)
def eucl(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0
def eof(t): print(t); exit()

import itertools
l=list(itertools.combinations(range(24),12))

n,m=map(int,input().split())
ans=chk=0
if n>12 or m>12:
    exit()
a=[]
for i in range(n):
    y,s,p=map(int,input().split())
    a.append((y,s,p))
b=[]
for i in range(m):
    y,s,p=map(int,input().split())
    b.append((y,s,p))

for i in l:
    x=[0]*24
    for j in i:
        x[j]=1
    io=jo=0
    chk=ti=0
    for j in x:
        if j==0 and io<n:
            ti+=a[io][0]
            if ti<=a[io][1]:
                chk+=a[io][2]
            io+=1
        if j==1 and jo<m:
            ti+=b[jo][0]
            if ti<=b[jo][1]:
                chk+=b[jo][2]
            jo+=1
    ans=max(ans,chk)
            
print(ans)
