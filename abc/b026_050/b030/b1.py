#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n,m=map(int,raw_input().split())
n%=12
n=(30.0*n)+(m*0.5)
m=m*6.0
print "{0:.10f}".format(min(abs(n-m),360-abs(n-m)))
