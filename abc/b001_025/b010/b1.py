#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
#10**9+7
mod=1000000007
#start = time.clock()
n=raw_input()
l=map(int,raw_input().split())
ans=chk=0

def hana(h):
    d=[2,4,5,6,8,10]
    k=0
    if h in d:
        while h in d:
            h-=1
            k+=1
    return k

ans=0
for i in l:
    ans+=hana(i)
print ans
#end = time.clock()
#print end - start
