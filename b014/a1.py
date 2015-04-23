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
a=input()
b=input()
if a-b==0:
    print 0
elif a>b:
    print b-(a%b)
else:
    print b-a
#end = time.clock()
#print end - start
