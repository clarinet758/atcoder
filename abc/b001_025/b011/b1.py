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
s=raw_input()
ans=''
for a,i in enumerate(s):
    if a==0:
        ans+=i.upper()
    else:
        ans+=i.lower()
print ans
