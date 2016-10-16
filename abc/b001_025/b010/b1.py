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
a=[0,0,1,0,1,2,3,0,1,0,1]
l=map(int,raw_input().split())
ans=chk=0
for i in l:
    ans+=a[i]
print ans
#end = time.clock()
#print end - start
