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
#start = time.clock()
n,m=map(int,raw_input().split())
ans=chk=0
l,bus=[],[]
for i in xrange(n+1):
    bus.append([])
    bus[i]=[0 for _ in xrange(n+1)]
for i in xrange(m):
    a,b,c=map(int, raw_input().split())
#    l.append((a,b,c))
    bus[a][b]=c
    bus[b][a]=c
#print l

#print bus
for i in xrange(1,n+1):
    for j in xrange(1,n+1):
        if i==j or bus[i][j]:
            pass
        else:
            for k in xrange(1,n+1):
                if bus[k][j] and bus[i][k]:
                    bus[i][j]=bus[i][k]+bus[k][j]
                    bus[j][i]=bus[i][k]+bus[k][j]
ans=max(bus[1])
for i in xrange(1,n+1):
    ans=min(ans,max(bus[i]))
print ans

#end = time.clock()
#print end - start
