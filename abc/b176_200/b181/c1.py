#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def tri(xa,ya,xb,yb,xc,yc): return abs((xa-xc)*(yb-yc)-(xb-xc)*(ya-yc))

n=int(input())
w=[]
for i in range(n):
    x,y=map(int,input().split())
    w.append((x,y))
ans=1
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            ans=min(ans,tri(w[i][0],w[i][1],w[j][0],w[j][1],w[k][0],w[k][1]))
print("No" if ans else "Yes")
