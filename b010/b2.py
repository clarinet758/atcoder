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
#mod=1777777777
pi=3.141592653589
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
#start = time.clock()
s=[9,7,3,1]
n=int(raw_input())
l=map(int,raw_input().split())
ans=chk=0
for i in l:
    for j in s:
        if i==j:
            break
        elif i>j:
            ans+=(i-j)
            break
print ans
#end = time.clock()
#print end - start
