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

X=raw_input()
l=[0,0]
for i in X:
    if i=='S':
        l[0]+=1
    elif i=='T' and l[0]>0:
        l[0]-=1
    else:
        l[1]+=1
print sum(l)
exit()
while 1:
    if 'SSSSSSSSSSSSSSSSSSSSSSSSSTTTTTTTTTTTTTTTTTTTTTTTTT' in X:
       X=X.replace('SSSSSSSSSSSSSSSSSSSSSSSSSTTTTTTTTTTTTTTTTTTTTTTTTT','')
    elif 'SSSSSSSSSSSSSSSSSSSSTTTTTTTTTTTTTTTTTTTT' in X:
       X=X.replace('SSSSSSSSSSSSSSSSSSSSTTTTTTTTTTTTTTTTTTTT','')
    elif 'SSSSSSSSSSSSSSSTTTTTTTTTTTTTTT' in X:
       X=X.replace('SSSSSSSSSSSSSSSTTTTTTTTTTTTTTT','')
    elif 'SSSSSSSSSSTTTTTTTTTT' in X:
       X=X.replace('SSSSSSSSSSTTTTTTTTTT','')
    elif 'SSSSSSSTTTTTTT' in X:
       X=X.replace('SSSSSSSTTTTTTT','')
    elif 'SSSSSTTTTT' in X:
       X=X.replace('SSSSSTTTTT','')
    elif 'SSSTTT' in X:
       X=X.replace('SSSTTT','')
    elif 'ST' in X:
       X=X.replace('ST','')
    else:
        break
print len(X)
exit()
n,k=map(int,raw_input().split())
l=map(int,raw_input().split())
ans=chk=0
#end = time.clock()
#print end - start
