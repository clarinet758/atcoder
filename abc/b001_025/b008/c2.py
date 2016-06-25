#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
#start = time.clock()
#refer from http://abc008.contest.atcoder.jp/submissions/169691

p=[1.0]
c=[[0.0 for j in xrange(106)] for i in xrange(106)]

for i in xrange(105):
    c[i][0]=1.0
    for j in xrange(1,i+1):
        c[i][j]=c[i-1][j-1]+c[i-1][j]
    p.append(p[-1]*(i+1.0))
n=int(raw_input())
s=[]
for i in xrange(n):
    s.append(int(raw_input()))

ret=0.0
for x in xrange(n):
    mul=0
    for y in xrange(n):
        if x!=y and (s[x]%s[y]==0):
            mul+=1
    for z in xrange(0,mul+1,2):
        ret+=c[mul][z]*p[mul-z]*p[z]/p[mul+1]
print ret
#end = time.clock()
#print end - start
