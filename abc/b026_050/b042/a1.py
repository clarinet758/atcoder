#!/usr/bin/env python
# -*- coding: UTF-8 -*-

l=map(int,raw_input().split())
l.sort()
print 'YES' if l[0]==l[1]==5 and l[2]==7 else 'NO'
