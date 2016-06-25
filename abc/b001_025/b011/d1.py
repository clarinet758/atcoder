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
for i in range(n):
    chk1=list(chk1)
    if (x,y) in chk1:
        print 1/float(len(chk1))
        exit()
    for i in chk1:
        chk2.append((i[0]+d,i[1]))
        chk2.append((i[0]-d,i[1]))
        chk2.append((i[0],i[1]+d))
        chk2.append((i[0],i[1]-d))
    chk1=chk2
    chk2=chk2[:]
print '0.0'



#end = time.clock()
#print end - start
