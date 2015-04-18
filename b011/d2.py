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
n,d=map(int,raw_input().split())
x,y=map(int,raw_input().split())
chk1=[(0,0)]
chk2=[]
if x%d or y%d:
    print '0.0'
    exit()
for i in range(n):
    while len(chk1)>0:
        a,b=chk1.pop()
        chk2.append((a+d,b))
        chk2.append((a-d,b))
        chk2.append((a,b+d))
        chk2.append((a,b-d))
    chk1=chk2[:]
    chk2=[]
#    if (x,y) in chk1:
#        print chk1.count((x,y))/float(len(chk1))
#        exit()
print '0.0' if (x,y) not in chk1 else chk1.count((x,y))/float(len(chk1))


#end = time.clock()
#print end - start
