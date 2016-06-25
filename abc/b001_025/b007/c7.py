#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
#start = time.clock()
r,c=map(int,raw_input().split())
s=map(int,raw_input().split())
g=map(int,raw_input().split())
boad=[]
q=[(s[0]-1,s[1]-1)]
m=[(1,0),(0,1),(-1,0),(0,-1)]
for i in range(r):
    boad.append(list(raw_input()))
boad[s[0]-1][s[1]-1]=0
while 1:
    chk=q.pop(0)
    for y,x in m:
        if boad[chk[0]+y][chk[1]+x]=='.':
            if chk[0]+y==g[0]-1 and chk[1]+x==g[1]-1:
                print boad[chk[0]][chk[1]]+1
                exit()
            boad[chk[0]+y][chk[1]+x]=boad[chk[0]][chk[1]]+1
            q.append((chk[0]+y,chk[1]+x))




#end = time.clock()
#print end - start
