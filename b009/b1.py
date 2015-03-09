#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
#10**9+7
mod=1000000007
#start = time.clock()
n=int(raw_input())
a=set()
while n:
    n-=1
    a.add(input())
a=list(a)
a.sort()
print a[-2]

#end = time.clock()
#print end - start
