#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n,k=map(int,raw_input().split())
chk=1
if k-1>0 and k<n:
    chk+=(k-1)*(n-k)*6
if k<n:
    chk+=(n-k)*3
if k-1>0:
    chk+=(k-1)*3
print chk*1.0/(n**3)
