#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
#start = time.clock()
n=int(raw_input())
ans=0
l=[]
for i in xrange(n):
    l.append(int(raw_input()))
chk=[0 for _ in range(n)]
for i in range(n):
    cnt=0
    for j in range(n):
        if i!=j and l[i]%l[j]==0:
            cnt+=1
    chk[i]=cnt
a=b=0
for i in range(n):
    if chk[i]%2:
        a+=1
        b+=2
    else:
        a+=(chk[i]+2)
        b+=(2*chk[i]+2)
print chk
print (1.0*a/b),(1.0/len(chk))
print (1.0*a/b)*(1/len(chk))
        

#end = time.clock()
#print end - start
