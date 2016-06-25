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
def euclid_dis2(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0

ans=[0]*3
n=int(raw_input())
l=[]
boat=[[0]*n for _ in range(n)]
for i in range(n):
    a,b=map(int,raw_input().split())
    l.append((a,b))
for i in range(n-2):
    for j in range(i+1,n-1):
        if boat[i][j]==0:
            a=euclid_dis2(l[i][0],l[i][1],l[j][0],l[j][1])
        else:
            a=boat[i][j]
        for k in range(j+1,n):
            if boat[i][k]==0:
                b=euclid_dis2(l[i][0],l[i][1],l[k][0],l[k][1])
            else:
                b=boat[i][k]
            if boat[k][j]==0:
                c=euclid_dis2(l[k][0],l[k][1],l[j][0],l[j][1])
            else:
                c=boat[k][j]
            tmp=[a,b,c]
            tmp.sort()
            A=tmp[0]
            B=tmp[1]
            C=tmp[2]
            if A+B==C:
                ans[1]+=1
            elif A+B<C:
                ans[2]+=1
            else:
                ans[0]+=1
print ' '.join(map(str,ans))

#l=map(int,raw_input().split())
ans=chk=0
#end = time.clock()
#print end - start
