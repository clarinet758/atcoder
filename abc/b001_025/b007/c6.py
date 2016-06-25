#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
#start = time.clock()

#162258 のkusanoさんのパクリです。
r,c=map(int,raw_input().split())
sy,sx=[int(i)-1 for i in raw_input().split()]
gy,gx=[int(i)-1 for i in raw_input().split()]
cw=[raw_input() for _ in range(r)]
t=[[-1]*c for _ in range(r)]
t[sy][sx]=0
q=[(sx,sy)]

while t[gy][gx]==-1:
    fx,fy=q.pop(0)
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        tx,ty=fx+dx,fy+dy
        if cw[ty][tx]=='.' and t[ty][tx]==-1:
            t[ty][tx]=t[fy][fx]+1
            q+=[(tx,ty)]
print t[gy][gx]
#end = time.clock()
#print end - start
