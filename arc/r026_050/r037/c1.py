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
n,k=map(int,raw_input().split())
x=map(int,raw_input().split())
y=map(int,raw_input().split())
ans=-1
x.sort()
y.sort()
a=x.pop(0)
b=y.pop(0)
k-=1
ans=a*b
while k:
    k-=1
    if len(x) and len(y):
        if x[0]<y[0]:
            a=x.pop(0)
            ans=a*b
        else:
            b=y.pop(0)
            ans=a*b
    elif len(x):
        a=x.pop(0)
        ans=a*b
    elif len:
        b=y.pop(0)
        ans=a*b
print ans


print ans

#end = time.clock()
#print end - start
