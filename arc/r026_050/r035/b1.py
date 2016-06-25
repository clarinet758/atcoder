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
#mod=1777777777
pi=3.141592653589
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
#start = time.clock()
n=int(raw_input())
l=[0]*10001
chk=1
ans=t=0
def kai(x):
    a=1
    for i in range(1,x+1):
        a*=i
    return a

def pen(y,z):
    b=0
    for j in range(1,z+1):
        b+=y*j
    return b

for i in range(n):
    s=int(raw_input())
    l[s]+=1

for i in range(10001):
    if l[i]!=0:
        for k in range(1,l[i]+1):
            t+=i
            ans+=t
        chk*=kai(l[i])
print ans
print chk%mod
#end = time.clock()
#print end - start
