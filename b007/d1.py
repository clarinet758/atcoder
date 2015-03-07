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
a,b=map(int,raw_input().split())
ans=0
for i in xrange(a,b+1):
    chk=str(i)
    if '4' in chk or '9' in chk:
        ans+=1
print ans
#end = time.clock()
#print end - start
