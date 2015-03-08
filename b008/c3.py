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
l=[]
for i in xrange(n):
    l.append(int(raw_input()))

def sol(x,p):
    x=list(x)
    for i in xrange(p-1):
        for j in xrange(i+1,p):
            if x[j]%x[i]==0:
                x[j]*=-1
    return len([i for i in x if i>0])
ans=k=0
chk=list(itertools.permutations(l))
for i in range(len(chk)):
    if i>0 and chk[i-1]==chk[i]:
        ans+=k
    else:
        k=sol(chk[i],n)
        ans+=k
print ans*1.0/len(chk)
    
#end = time.clock()
#print end - start
