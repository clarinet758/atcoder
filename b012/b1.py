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
ans=[]
ans.append(n/3600)
ans.append((n%3600)/60)
ans.append(n%60)
for i in range(3):
    ans[i]="{0:0>2}".format(ans[i])
print ':'.join(map(str,ans))


