#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
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
def fib(n): return [(seq.append(seq[i-2] + seq[i-1]), seq[i-2])[1] for seq in [[0, 1]] for i in range(2, n)]
def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)
def eucl(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0
def pscl(num,l=[1]):
    for i in range(num):
        l = map(lambda x,y:x+y,[0]+l,l+[0])
    return l

#n=int(raw_input())
h,w=map(int,raw_input().split())
l=[]
#l=map(int,raw_input().split())
for i in range(h):
    l.append(list(raw_input()))
l[0][0]='.'
x=y=0
while 1:
    if x+1<w and l[y][x+1]=='#':
        x+=1
        l[y][x]='.'
    elif y+1<h and l[y+1][x]=='#':
        y+=1
        l[y][x]='.'
    else:
        break
for i in l:
    if '#' in i:
        print 'Impossible'
        exit()
print 'Possible'

ans=chk=0
#end = time.clock()
#print end - start
