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
ans=0
chk=2025-n
for i in range(1,10):
    for j in range(1,10):
        if i*j==chk:
            print ' x '.join(map(str,(i,j)))
#print end - start
