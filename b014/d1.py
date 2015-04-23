#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
from copy import deepcopy
#10**9+7
mod=1000000007
ans=0
n=int(raw_input())
l=[[0 for i in xrange(n)] for j in xrange(n)]
for i in xrange(n-1):
    a,b=map(int,raw_input().split())
    l[a-1][b-1]=1
    l[b-1][a-1]=1
q=int(raw_input())
for i in xrange(q):
    lc=deepcopy(l)
    j,c=map(int,raw_input().split())
    lc[j-1][c-1]=1
    lc[c-1][j-1]=1
    chk=1
    while chk:
        chk=0
        for i in xrange(n):
            if lc[i].count(1)==1:
                f=lc[i].index(1)
                lc[f][i]=0
                lc[i][f]=0
                chk=1
    ka=0
    for i in xrange(n):
        if 1 in lc[i]:
            ka+=1
    print ka

#end = time.clock()
#print end - start
