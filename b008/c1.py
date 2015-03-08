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
chk=list(itertools.permutations(l))
chk=set(chk)
chk=list(chk)
for i in range(len(chk)):
    t=[1 for x in range(len(chk[i]))]
    for j in range(0,len(chk[i])-1):
        for k in range(j+1,len(chk[i])):
            if chk[i][k]%chk[i][j]==0:
                if t[k]==0:
                    t[k]=1
                else:
                    t[k]=0
    ans+=t.count(1)
print 1.0*ans/len(chk)
        

#end = time.clock()
#print end - start
