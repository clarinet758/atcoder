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
def niten(a,b): return abs(a-b) if a>=0 and b>=0 else  a+abs(b) if a>=0 else abs(a)+b if b>=0 else abs(abs(a)-abs(b))
def fib(n): return [(seq.append(seq[i-2] + seq[i-1]), seq[i-2])[1] for seq in [[0, 1]] for i in range(2, n)]
def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)
def eucl(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0
#def pscl(num,l=[1]):
#    for i in range(num):
#        l = map(lambda x,y:x+y,[0]+l,l+[0])
#    return l
# fractions.gcd(x,y)
# pscl 要修正
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
x,y,w=input().split()
x=int(x)-1
y=int(y)-1
d={"D":[1,0],"U":[-1,0],"R":[0,1],"L":[0,-1],"RD":[1,1],"LD":[1,-1],"RU":[-1,1],"LU":[-1,-1]}
l=[input() for i in range(9)]
ans=l[y][x]
for i in range(3):
    if y==0 and x==0 and len(w)>1: w="RD"
    if y==8 and x==0 and len(w)>1: w="RU"
    if y==8 and x==8 and len(w)>1: w="LU"
    if y==0 and x==8 and len(w)>1: w="LD"
    
    if 0<=y+d[w][0]<9 and  0<=x+d[w][1]<9:
        pass
    elif w in ("R","L","U","D"):
        if w=="R": w="L"
        elif w=="L": w="R"
        elif w=="U": w="D"
        else: w="U"
    elif y==0:
        if w=="RU": w="RD"
        elif w=="LU": w="LD"
    elif x==8:
        if w=="RU": w="LU"
        elif w=="RD": w="LD"
    elif y==8:
        if w=="LD": w="LU"
        elif w=="RD": w="RU"
    elif x==0:
        if w=="LD": w="RD"
        elif w=="LU": w="RU"
    y+=d[w][0]
    x+=d[w][1]
    ans+=l[y][x]
#    print(w,y,x)
print(ans)
