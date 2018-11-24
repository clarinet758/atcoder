#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
mod=1000000007
xy=[(1,0),(-1,0),(0,1),(0,-1)]

h,w,t=map(int,input().split())
s=[]
for i in range(h):
    a=input()
    s.append(a)
    if "S" in a: x=(i,a.index("S"))
    if "G" in a: y=(i,a.index("G"))
p,q=0,t
for i in range(100):
    c=[[mod for i in range(w)] for j in range(h)]
    c[x[0]][x[1]]=0
    c[y[0]][y[1]]=0
    now=set()
    now.add(x)
    k=(p+q)//2
    while len(now):
        d,e=now.pop()
        for i,j in xy:
            if 0<=i+d<h and 0<=j+e<w:
                if s[i+d][j+e]=="#":
                    if c[i+d][j+e]>c[d][e]+k and t>c[d][e]+k:
                        c[i+d][j+e]=c[d][e]+k
                        now.add(((i+d),(j+e)))
                elif s[i+d][j+e]=="." :
                    if c[i+d][j+e]>c[d][e]+1 and t>c[d][e]+1:
                        c[i+d][j+e]=c[d][e]+1
                        now.add(((i+d),(j+e)))
                else:
                    if c[i+d][j+e]<=c[d][e]+1<=t:
                        c[i+d][j+e]=c[d][e]+1
    if c[y[0]][y[1]]:p=k
    else: q=k
    if q-p<2: break

print(p)
