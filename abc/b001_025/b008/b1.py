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
#n,k=map(int,raw_input().split())
#l=[int(x) for x in raw_input().split()]
ans=['',0]
d={}
for i in range(n):
    s=raw_input()
    if s in d:
        d[s]+=1
    else:
        d[s]=1
    if d[s]>ans[1]:
        ans=[s,d[s]]
print ans[0]

#end = time.clock()
#print end - start
