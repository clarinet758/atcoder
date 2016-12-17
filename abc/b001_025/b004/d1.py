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

def cost(ichi,nokori):
    if(nokori>=g+b): return abs(400-ichi)
    elif(nokori>=b): return abs(500-ichi)
    else: return abs(600-ichi)

r,g,b=map(int,raw_input().split())
tmp=r+g+b
dp=[[IS if i!=tmp else 0 for i in range(1000)] for j in range(1000)]

for i in range(1,1000):
    for j in range(tmp):
        dp[i][j]=min(dp[i-1][j], dp[i-1][j+1]+cost(i,j))

ans=chk=IS
for i in range(1000):
    ans=min(ans,dp[i][0])
print ans
