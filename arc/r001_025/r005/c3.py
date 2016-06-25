#!/usr/bin/env python
# -*- coding:utf-8 -*-
import timeit
import time
import sys
import io
import re
import math
#start = time.time()
start = time.clock()
H,W=[int(x)+2 for x in raw_input().split()]
c=['$'*W]+['$'+raw_input()+'$' for _ in range(H-2)]+['$'*W]
D=[[9]*W for _ in range(H)]
#Q=[[],[],[]]

for y in range(H):
    for x in range(W):
        if c[y][x]=='s':
            D[y][x]=0
            Q=[[(x,y)],[],[]]

for q in Q:
    while len(q)>0:
        x,y=q.pop()
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            tx,ty=x+dx,y+dy
            if c[ty][tx]=='#':
                d=D[y][x]+1
            elif c[ty][tx]=='$':
                d=3
            else:
                d=D[y][x]
            if d<=2 and d<D[ty][tx]:
                D[ty][tx]=d
                Q[d]+=[(tx,ty)]
for y in range(H):
    for x in range(W):
        if c[y][x]=='g':
            print 'YES' if D[y][x]<=2 else 'NO'

end = time.clock()
print end - start
