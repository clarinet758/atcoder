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
ng=[]
e=[3,2,1]
ans=['NO','YES']
for i in range(3):
    ng.append(int(raw_input()))

def sim(a,dame,hiku):
    g=100
    while g:
        g-=1
        for i in hiku:
            if a-i not in dame:
                a-=i
                break
            elif i==1:
                return 0
        if a<=0:
            return 1
    return 0

print ans[sim(n,ng,e)]



#end = time.clock()
#print end - start
