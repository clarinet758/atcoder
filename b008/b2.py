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
w={}
for i in xrange(n):
    s=raw_input()
    if w.has_key(s):
        w[s]+=1
    else:
        w[s]=1
ans=''
chk=0
for i in w:
    if chk<w[i]:
        chk=w[i]
        ans=i
print ans
        
#end = time.clock()
#print end - start
