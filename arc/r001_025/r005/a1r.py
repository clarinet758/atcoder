#!/usr/bin/env python
# -*- coding:utf-8 -*-
import timeit
import time
import sys
import io
import re
import math
#start = time.time()
start = time.clock()
i = 0
n = input()
w = map(str, raw_input()[:-1].split())
t = ['TAKAHASHIKUN','Takahashikun','takahashikun']

for x in xrange(3):
    i+=w.count(t[x])
#    print x
print i
#print n,w
#while i < 10000:
#    time.sleep(1)
#    i+=1
#print i
end = time.clock()
print end - start
