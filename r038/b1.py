#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
#sys.stdin=file('input.txt')
#sys.stdout=file('output.txt','w')
#10**9+7
mod=1000000007
#mod=1777777777
pi=3.141592653589
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
mv=[(1,0),(0,1),(1,1)]
#start = time.clock()
h,w=map(int,raw_input().split())
#l=map(int,raw_input().split())
l=[]
q=[(0,0)]
for i in range(h):
    l.append(list(raw_input()))
ans=chk=0
l[0][0]=0
while len(q):
    y,x=q.pop(0)
    for dy,dx in mv:
        ty,tx=y+dy,x+dx
        if ty+1<=h and tx+1<=w:
            if l[ty][tx]=='#' or ty+1>h or tx+1>w:
                pass
            elif l[ty][tx]=='.':
                l[ty][tx]=l[y][x]+1
                q.append((ty,tx))
            elif l[ty][tx]+1>l[y][x]+1:
                l[ty][tx]=l[y][x]+1
                q.append((ty,tx))
print 'First' if l[h-1][w-1]%2 else 'Second'

#end = time.clock()
#print end - start
