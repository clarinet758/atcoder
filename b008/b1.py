#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
#start = time.clock()
n=int(raw_input())
#n,k=map(int,raw_input().split())
#l=[int(x) for x in raw_input().split()]
ans=0
l=[]
for i in xrange(n):
    w=raw_input()
    l.append(w)
c=set(l)
c=list(c)
for i in range(len(c)):
    s=l.count(c[i])
    if s>=ans:
        chk=c[i]
    ans=max(ans,s)
print chk
#end = time.clock()
#print end - start
