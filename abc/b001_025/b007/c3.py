#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
#start = time.clock()
#n=int(raw_input())
r,c=map(int,raw_input().split())
sy,sx=map(int,raw_input().split())
gy,gx=map(int,raw_input().split())
#l=[int(x) for x in raw_input().split()]
k,g,tmp=[],[[sy-1,sx-1]],[]

ans=chk=0
l=[[] for _ in range(r)]
for i in range(r):
    l[i]=list(raw_input())
while 1:
#    k=list(k)
#    g=list(g)
    for i in range(len(g)):
        if g[i][1]>0:
            if l[g[i][0]][g[i][1]-1]=='.':
#                tmp.add([g[i][0],g[i][1]-1])
                tmp.append([g[i][0],g[i][1]-1])
        if g[i][0]<r-1:
            if l[g[i][0]+1][g[i][1]]=='.':
#                tmp.add(l[g[i][0]+1][g[i][1]])
                tmp.append([g[i][0]+1,g[i][1]])

        if g[i][1]<c-1:
            if l[g[i][0]][g[i][1]+1]=='.':
#                tmp.add([g[i][0],g[i][1]+1])
                tmp.append([g[i][0],g[i][1]+1])
        if g[i][0]>0:
            if l[g[i][0]-1][g[i][1]]=='.':
#                tmp.add(l[g[i][0]-1][g[i][1]])
                tmp.append([g[i][0]-1,g[i][1]])
        if (gy-1,gx-1) in g:
            print ans
            sys.exit()
        k+=g
        g+=tmp
    print g
#        print tmp
#    k=set(k)
#    g=set(g)
    ans+=1

    

#end = time.clock()
#print end - start
