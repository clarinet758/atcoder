#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
import re
import math
import itertools
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

def div(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors

n=int(input())
at=[int(i) for i in input().split()]
a=set(at)
d={}
for i,j in enumerate(a):
    t=div(j)
    for k in t:
        if k in d:
            d[k]+=1
        elif i==0 or k not in d:
            d[k]=1
ans=1
for i in d:
    x=0
    for j in at:
        if j%i: x+=1
    if x<2: ans=max(ans,i)
print(ans)
