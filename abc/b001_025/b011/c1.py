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
#n,k=map(int,raw_input().split())
#l=[int(x) for x in raw_input().split()]
l=[]
for i in range(3):
    l.append(int(raw_input()))
if n in l:
    print 'NO'
    exit()
t=100
while t:
    t-=1
    if n-3 not in l and n-3>=0:
        n-=3
    elif n-2 not in l and n-2>=0:
        n-=2
    elif n-1 not in l and n-1>=0:
        n-=1
    else:
        break
    if n==0:
        break
print 'YES' if n==0 else 'NO'

#end = time.clock()
#print end - start
