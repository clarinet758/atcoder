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
n,X=map(int,raw_input().split())
l=[int(x) for x in raw_input().split()]
bx=str(bin(X))[2::]
bx='0'*(n-len(bx))+bx
bx=bx[::-1]
ans=0
for i in range(n):
    if bx[i]=='1':
        ans+=l[i]
print ans
#end = time.clock()
#print end - start
