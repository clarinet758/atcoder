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
n,k=map(int,raw_input().split())
l=[int(x) for x in raw_input().split()]
ans=chk=0
#end = time.clock()
#print end - start
