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
#n,m=map(int,raw_input().split())
n=int(raw_input())
print "{0:02d}:{1:02d}:{2:02d}".format(n/3600,n%3600/60,n%60)

#end = time.clock()
#print end - start
