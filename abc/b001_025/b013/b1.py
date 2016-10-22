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
ans=[0,1,2,3,4,5,4,3,2,1]
a=int(raw_input())
b=int(raw_input())
print ans[b-a]
exit()
n,k=map(int,raw_input().split())
l=[int(x) for x in raw_input().split()]
ans=chk=0
#end = time.clock()
#print end - start
