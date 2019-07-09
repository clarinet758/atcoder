#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,l=map(int,input().split())
w=[]
for i in range(l):
    w.append(input())
o=input()
g=o.index("o")
x=len(w[0])-1
for i in range(-1,-l-1,-1):
    if g==0 and x!=0 and w[i][g+1]=="-":
            g+=2
    elif 0<g<x and w[i][g+1]=="-":
            g+=2
    elif 0<g<x and w[i][g-1]=="-":
            g-=2
    elif g==x and x!=1 and w[i][g-1]=="-":
            g-=2
print(g//2+1)
