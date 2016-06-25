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
n,h=map(int,raw_input().split())
a,b,c,d,e=map(int,raw_input().split())
total=chk=0
for i in xrange(n):
    for j in xrange(n):
        for k in xrange(n):
#end = time.clock()
#print end - start
