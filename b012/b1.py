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
h=n/3600
m=(n-(h*3600))/60
s=n%60
print "%02d:%02d:%02d"%(h,m,s)
#end = time.clock()
#print end - start
