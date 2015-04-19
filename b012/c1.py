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
ans=chk=0
for i in xrange(1,10):
    for j in xrange(1,10):
        if i*j==2025-n:
            print i,'x',j

#end = time.clock()
#print end - start
