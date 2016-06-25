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

n=int(raw_input())
l=[]
for i in range(n):
    r,h=map(int,raw_input().split())
    l.append((r,h))
res={i:[0,0,0] for i in range(n)}
sute=range(n)
for i in sute:
    for j in sute:
        #print res
        #print l[i],l[j]
        if i>=j:
            pass
        elif l[i][0]>l[j][0]:
            res[i][0]+=1
            res[j][1]+=1
        elif l[i][0]==l[j][0]:
            tmp=l[i][1]+1
            if tmp>3:
                tmp=1
            if l[j][1]==tmp:
                res[i][0]+=1
                res[j][1]+=1
            elif l[i][1]==l[j][1]:
                res[i][2]+=1
                res[j][2]+=1
            else:
                res[i][1]+=1
                res[j][0]+=1
        else:
            res[i][1]+=1
            res[j][0]+=1
for i in sute:
    print ' '.join(map(str,res[i]))
exit()
l=map(int,raw_input().split())
ans=chk=0
#end = time.clock()
#print end - start
