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
n=int(raw_input())
l=[0 for i in xrange(1000002)]
for i in xrange(n):
    a,b=map(int,raw_input().split())
    l[a]+=1
    l[b+1]-=1
ans=chk=0
for i in l:
    chk+=i
    ans=max(ans,chk)
print ans
#end = time.clock()
#print end - start
