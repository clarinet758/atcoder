#!/usr/bin/env python
# -*- coding: UTF-8 -*-
a,b=map(int,raw_input().split())
ans=0
if b>10000:
    print 0
    exit()
for i in range(a,b+1):
    i=str(i)
    if '4' in i or '9' in i:
        ans+=1
print ans
