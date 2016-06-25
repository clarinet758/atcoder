#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
#start = time.clock()
w,h=map(int,raw_input().split())
n=int(raw_input())
ans=0
l=[['#' for i in range(w)] for j in range(h)]
que=[]
for i in range(n):
    x,y=map(int,raw_input().split())
    que.append((-y,x-1))

#map,q
def sol(b,q):
    news=[(-1,0),(0,1),(0,-1),(1,0)]
    cnt=0
    for i in q:
        for j in news:
            now=[i[0],i[1]]
            if b[now[0]][now[1]]!='*':
               b[now[0]][now[1]]='*'
               cnt+=1
            while 1:
                now[0]+=j[0]
                now[1]+=j[1]
                if now[0]>0 or now[0]<-h or now[1]<0 or now[1]>=w:
                    break
                elif b[now[0]][now[1]]=='*':
                    break
                else:
                    b[now[0]][now[1]]='*'
                    cnt+=1

    return cnt

chk=list(itertools.permutations(que,n))
for i in chk:
    ans=max(ans,sol(l,i))
print ans





#end = time.clock()
#print end - start
